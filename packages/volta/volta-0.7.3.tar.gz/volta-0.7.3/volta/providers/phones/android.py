""" Android phone worker, OS version >5

"""
import logging
import re
import pkg_resources
import time
import threading
import subprocess
import pandas as pd

from netort.data_processing import Drain, get_nowait_from_queue
from netort.resource import manager as resource

from volta.common.interfaces import Phone
from volta.common.util import LogParser, Executioner

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)  # pandas sorting warnings


logger = logging.getLogger(__name__)

event_regexp = r"""
    ^(?P<date>\S+)
    \s+
    (?P<time>\S+)
    \s+
    \S+
    \s+
    \S+
    \s+
    \S+
    \s+
    \S+
    \s+
    (?P<value>.*)
    $
    """


class AndroidPhone(Phone):
    """ Android phone worker class - work w/ phone, read phone logs, run test apps and store data

    Attributes:
        source (string): path to data source, phone id (adb devices)
        lightning_apk_path (string, optional): path to lightning app
            may be url, e.g. 'http://myhost.tld/path/to/file'
            may be path to file, e.g. '/home/users/netort/path/to/file.apk'
        lightning_apk_class (string, optional): lightning class
        test_apps (list, optional): list of apps to be installed to device for test
        test_class (string, optional): app class to be started during test execution
        test_package (string, optional): app package to be started during test execution
        test_runner (string, optional): app runner to be started during test execution

    """

    def __init__(self, config, core):
        """
        Args:
            config (VoltaConfig): module configuration data
        """
        Phone.__init__(self, config, core)
        self.logcat_stdout_reader = None
        self.logcat_stderr_reader = None

        # mandatory options
        self.source = config.get_option('phone', 'source')

        # lightning app configuration
        self.lightning_apk_path = config.get_option(
            'phone', 'lightning', pkg_resources.resource_filename(
                'volta.providers.phones', 'binary/lightning-new3.apk'
            )
        )
        self.lightning_apk_class = config.get_option('phone', 'lightning_class')
        self.lightning_apk_fname = None

        # test app configuration
        self.test_apps = config.get_option('phone', 'test_apps')
        self.test_class = config.get_option('phone', 'test_class')
        self.test_package = config.get_option('phone', 'test_package')
        self.test_runner = config.get_option('phone', 'test_runner')
        self.cleanup_apps = config.get_option('phone', 'cleanup_apps')
        try:
            self.compiled_regexp = re.compile(
                config.get_option('phone', 'event_regexp', event_regexp), re.VERBOSE | re.IGNORECASE
            )
        except SyntaxError:
            logger.debug('Unable to parse specified regexp', exc_info=True)
            raise RuntimeError(
                "Unable to parse specified regexp: %s" % config.get_option('phone', 'event_regexp', event_regexp)
            )
        self.logcat_pipeline = None
        self.test_performer = None
        self.phone_q = None

        subprocess.call('adb start-server', shell=True)  # start adb server
        self.__test_interaction_with_phone()

        self.worker = None
        self.closed = False

        self.shellexec_metrics = config.get_option('phone', 'shellexec_metrics')
        self.shellexec_executor = threading.Thread(target=self.__shell_executor)
        self.shellexec_executor.setDaemon(True)
        self.shellexec_executor.start()

        self.my_metrics = {}
        self.__create_my_metrics()

    def __create_my_metrics(self):
        self.my_metrics['events'] = self.core.data_session.new_metric(
            {
                'type': 'events',
                'name': 'events',
                'source': 'phone'
            }
        )
        for key, value in self.shellexec_metrics.items():
            self.my_metrics[key] = self.core.data_session.new_metric(
                {
                    'type': 'metrics',
                    'name': key,
                    'source': 'phone',
                    '_apply': value.get('apply') if value.get('apply') else '',
                }
            )

    def __test_interaction_with_phone(self):
        def read_process_queues_and_report(outs_q, errs_q):
            outputs = get_nowait_from_queue(outs_q)
            for chunk in outputs:
                logger.debug('Command output: %s', chunk.strip())
                if chunk.strip() == 'unknown':
                    worker.close()
                    raise RuntimeError(
                        'Phone "%s" has an unknown state. Please check device authorization and state' % self.source
                    )

            errors = get_nowait_from_queue(errs_q)
            if errors:
                worker.close()
                raise RuntimeError(
                    'There were errors trying to test connection to the phone %s. Errors :%s' % (
                        self.source, errors
                    )
                )
        cmd = "adb -s {device_id} get-state".format(device_id=self.source)
        # get-state
        worker = Executioner(cmd)
        outs_q, errs_q = worker.execute()
        while worker.is_finished() is None:
            read_process_queues_and_report(outs_q, errs_q)
            time.sleep(1)
        read_process_queues_and_report(outs_q, errs_q)
        while not outs_q.qsize() != 0 and errs_q.qsize() != 0:
            time.sleep(0.5)
        worker.close()
        logger.info('Command \'%s\' executed on device %s. Retcode: %s', cmd, self.source, worker.is_finished())

    def adb_execution(self, cmd):
        def read_process_queues_and_report(outs_q, errs_q):
            outputs = get_nowait_from_queue(outs_q)
            for chunk in outputs:
                logger.debug('Command \'%s\' output: %s', cmd, chunk.strip())
            errors = get_nowait_from_queue(errs_q)
            for err_chunk in errors:
                logger.warning('Errors in command \'%s\' output: %s', cmd, err_chunk.strip())
        worker = Executioner(cmd)
        outs_q, errs_q = worker.execute()
        while worker.is_finished() is None:
            read_process_queues_and_report(outs_q, errs_q)
            time.sleep(1)
        read_process_queues_and_report(outs_q, errs_q)
        while not outs_q.qsize() != 0 and errs_q.qsize() != 0:
            time.sleep(0.5)
        worker.close()
        logger.info('Command \'%s\' executed on device %s. Retcode: %s', cmd, self.source, worker.is_finished())
        if worker.is_finished() != 0:
            raise RuntimeError('Failed to execute adb command \'%s\'' % cmd)

    def prepare(self):
        """ Phone preparation: install apps etc

        pipeline:
            install lightning
            install apks
            clean log
        """
        # apps cleanup
        for apk in self.cleanup_apps:
            self.adb_execution("adb -s {device_id} uninstall {app}".format(device_id=self.source, app=apk))

        # install lightning
        self.lightning_apk_fname = resource.get_opener(self.lightning_apk_path).get_filename
        logger.info('Installing lightning apk...')
        self.adb_execution(
            "adb -s {device_id} install -r -d -t {apk}".format(device_id=self.source, apk=self.lightning_apk_fname)
        )

        # install apks
        for apk in self.test_apps:
            apk_fname = resource.get_opener(apk).get_filename
            self.adb_execution("adb -s {device_id} install -r -d -t {apk}".format(device_id=self.source, apk=apk_fname))

        # clean logcat
        self.adb_execution("adb -s {device_id} logcat -c".format(device_id=self.source))

    def start(self, results):
        """ Grab stage: starts log reader, make sync w/ flashlight
        Args:
            results (queue-like object): Phone should put there dataframes, format: ['sys_uts', 'message']
        """
        self.phone_q = results
        self.__start_async_logcat()
        # start flashes app
        self.adb_execution(
            "adb -s {device_id} shell am start -n {package}/{runner}.MainActivity".format(
                device_id=self.source,
                package=self.lightning_apk_class,
                runner=self.lightning_apk_class
            )
        )
        logger.info('Waiting additional 15 seconds till flashlight app end its work...')
        time.sleep(15)

    def __start_async_logcat(self):
        """ Start logcat read in subprocess and make threads to read its stdout/stderr to queues """
        cmd = "adb -s {device_id} logcat".format(device_id=self.source)
        self.worker = Executioner(cmd)
        out_q, err_q = self.worker.execute()

        self.logcat_pipeline = Drain(
            LogParser(
                out_q, self.compiled_regexp, self.config.get_option('phone', 'type')
            ),
            self.my_metrics['events']
        )
        self.logcat_pipeline.start()

    def run_test(self):
        """ App stage: run app/phone tests """
        if self.test_package:
            cmd = "adb -s {device_id} shell am instrument -w -e class {test_class} {test_package}/{test_runner}".format(
                test_class=self.test_class,
                device_id=self.source,
                test_package=self.test_package,
                test_runner=self.test_runner
            )
        else:
            logger.info('Infinite loop for volta because there are no tests specified, waiting for SIGINT')
            cmd = '/bin/bash -c \'while [ 1 ]; do sleep 1; done\''
        logger.info('Command \'%s\' executing...', cmd)
        self.test_performer = Executioner(cmd)
        self.test_performer.execute()

    def end(self):
        """ Stop test and grabbers """
        self.closed = True
        if self.worker:
            self.worker.close()
        if self.test_performer:
            self.test_performer.close()
        if self.logcat_pipeline:
            self.logcat_pipeline.close()

        # apps cleanup
        for apk in self.cleanup_apps:
            self.adb_execution("adb -s {device_id} uninstall {app}".format(device_id=self.source, app=apk))

    def close(self):
        pass

    def get_info(self):
        data = {}
        if self.phone_q:
            data['grabber_queue_size'] = self.phone_q.qsize()
        if self.test_performer:
            data['test_performer_is_finished'] = self.test_performer.is_finished()
        return data

    def __shell_executor(self):
        while not self.closed:
            for key, value in self.shellexec_metrics.items():
                try:
                    if not self.shellexec_metrics[key].get('last_ts') \
                            or self.shellexec_metrics[key]['last_ts'] < int(time.time()) * 10**6:
                        metric_value = self.__execute_shellexec_metric(value.get('cmd'))
                        ts = int(time.time()) * 10 ** 6
                        if not value.get('start_time'):
                            self.shellexec_metrics[key]['start_time'] = ts
                            ts = 0
                        else:
                            ts = ts - self.shellexec_metrics[key]['start_time']
                            self.shellexec_metrics[key]['last_ts'] = ts
                        self.my_metrics[key].put(
                            pd.DataFrame(
                                data={
                                    ts:
                                        {'ts': ts, 'value': metric_value}
                                },
                            ).T
                        )
                    else:
                        continue
                except Exception:
                    logger.warning('Failed to collect shellexec metric: %s', key)
                    logger.debug('Failed to collect shellexec metric: %s', key, exc_info=True)

            time.sleep(0.1)

    @staticmethod
    def __execute_shellexec_metric(cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        (stdout, stderr) = proc.communicate()
        return stdout.strip()

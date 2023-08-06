import logging
import pandas as pd
import json
import yaml

from volta.listeners.uploader.uploader import DataUploader
from volta.core.core import VoltaConfig
from volta.core.config.dynamic_options import DYNAMIC_OPTIONS


logger = logging.getLogger(__name__)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='volta console post-loader')
    parser.add_argument('--debug', dest='debug', action='store_true', default=False)
    parser.add_argument('-l', '--logs', action='append', help='Log files list')
    parser.add_argument('-c', '--config', dest='config')
    args = parser.parse_args()

    logging.basicConfig(
        level="DEBUG" if args.debug else "INFO",
        format='%(asctime)s [%(levelname)s] [Volta Post-loader] %(filename)s:%(lineno)d %(message)s')

    config = {}
    PACKAGE_SCHEMA_PATH = 'volta.core'
    if not args.config:
        raise RuntimeError('config should be specified')

    if not args.logs:
        raise RuntimeError('Empty log list')

    with open(args.config, 'r') as cfg_stream:
        try:
            config = VoltaConfig(yaml.load(cfg_stream), DYNAMIC_OPTIONS, PACKAGE_SCHEMA_PATH)
        except Exception:
            raise RuntimeError('Config file not in yaml or malformed')

    uploader = DataUploader(config)
    uploader.create_job()

    for log in args.logs:
        try:
            with open(log, 'r') as logname:
                meta = json.loads(logname.readline())
        except ValueError:
            logger.warning('Skipped data file: no json header in logfile %s or json malformed...', log)
            logger.debug('Skipped data file: no json header in logfile %s or json malformed', log, exc_info=True)
            continue
        else:
            df = pd.read_csv(log, sep='\t', skiprows=1, names=meta['names'], dtype=meta['dtypes'])

        logger.info('Uploading %s, meta type: %s', log, meta['type'])

        uploader.put(df, meta['type'])

    logger.info('Updating job metadata...')
    try:
        update_job_data = {
            'test_id': config.get_option('core', 'test_id'),
            'name': config.get_option('uploader', 'name'),
            'dsc': config.get_option('uploader', 'dsc'),
            'device_id': config.get_option('uploader', 'device_id'),
            'device_model': config.get_option('uploader', 'device_model'),
            'device_os': config.get_option('uploader', 'device_os'),
            'app': config.get_option('uploader', 'app'),
            'ver': config.get_option('uploader', 'ver'),
            'meta': config.get_option('uploader', 'meta'),
            'task': config.get_option('uploader', 'task'),
        }
        uploader.update_job(update_job_data)
    except Exception:
        logger.warning('Exception updating metadata')

    uploader.close()
    logger.info('Done!')

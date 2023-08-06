from setuptools import setup, find_packages

setup(
    name='volta',
    version='0.7.3',
    description='yandex package for mobile energy consumption measurements',
    longer_description='''
yandex package for mobile energy consumption measurements
''',
    maintainer='Alexey Lavrenuke (load testing)',
    maintainer_email='direvius@yandex-team.ru',
    url='https://github.com/yandex-load/volta',
    packages=find_packages(exclude=["tests", "tmp", "docs", "data"]),
    python_requires='>=3',
    install_requires=[
        'tornado',
        'pandas>=0.23.0',
        'seaborn',
        'numpy>=1.11.0',
        'scipy',
        'matplotlib',
        'requests',
        'pyserial',
        'progressbar2',
        'pyusb',
        'pyyaml',
        'cerberus<1.2',
        'future',
        'netort==0.3.4',
        'retrying'
    ],
    setup_requires=[
    ],
    tests_require=[
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'volta = volta.api.cli:main',
            'volta-http = volta.api.http:main',
            'volta-uploader = volta.core.postloader:main',
            'volta-api = volta.api.manager:main'
        ],
    },
    license='MPLv2',
    package_data={
        'volta.providers.phones': ['binary/*.apk'],
        'volta.core': ['config/*'],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: POSIX',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Programming Language :: Python :: 3',
    ],
    use_2to3=False, )

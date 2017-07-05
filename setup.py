#!/usr/bin/env python

import setuptools

install_reqs = [
    'boto3'
]

setuptools.setup(
    name='cwgrep',
    author="Brian Elliott",
    description='CloudWatch Logs grep tool',
    url='https://github.com/bdelliott/cwgrep',
    version='0.0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_dir={'cwgrep': 'cwgrep'},
    install_requires=install_reqs,
    entry_points={
        'console_scripts': [
            'cwgrep = cwgrep.cli:main'
        ]
    },
)

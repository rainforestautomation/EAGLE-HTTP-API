#!/usr/bin/env python3

import os
from setuptools import setup,find_packages

__version__ = "0.1.0"

PACKAGE_NAME = 'eagle_http_api'
HERE = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_URL = ('https://github.com/bassclarinetl2/Eagle-Http-API/archive/' '{}.zip'.format(__version__))


PACKAGES = find_packages(exclude=['tests','tests.*'])

REQUIRES=[
	'lxml==3.4.2'
]


setup(
    name=PACKAGE_NAME,
    version=__version__,
    licence='MIT License',
    url='https://github.com/bassclarinetl2/Eagle-Http-API',
    download_url=DOWNLOAD_URL,
    author='Will Heid',
    author_email='bassclarinetl2@gmail.com',
    description='EAGLE Smart Meter Gateway python library',
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRES,
    keywords=['home','automation', 'power', 'monitoring'],
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Home Automation'
    ],
)



#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if sys.version_info[0] < 3:
    with open(os.path.join(BASE_DIR, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name='cabot-alert-webhooks',
    version='0.1.0',
    description='A Webhook plugin for Cabot',
    long_description=long_description,
    author='Nagarjuna Reddy C',
    author_email='nagarjuna@playment.in',
    url='https://github.com/arjunreddyc/cabot-alert-webhook',
    packages=find_packages(),
    download_url = 'https://github.com/arjunreddyc/cabot-alert-webhook/tarball/master',
    bugtrack_url = "https://github.com/arjunreddyc/cabot-alert-webhook/issues",
    keywords = ['cabot', 'webhook', 'status check'],
)

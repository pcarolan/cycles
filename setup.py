#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import sys
import re

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

version = ''
with open('cycles/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.rst', mode='r', encoding='utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', mode='r', encoding='utf-8') as f:
    history = f.read()

setup(
    name='cycles',
    version=version,
    description='A data processing framework.',
    long_description=readme + '\n\n' + history,
    url='https://github.com/pcarolan/cycles',
    author="Pat Carolan",
    author_email="patrick.carolan@gmail.com",
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.5'
    ],
    keywords='data etl processing',
    install_requires=[
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cycles=cycles:main',
        ],
    }
)

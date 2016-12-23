#!/usr/bin/env python
# coding: utf-8

import os
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with open(os.path.join(here, 'README.rst')) as f:
        return f.read()


def load_required_modules():
    with open(os.path.join(here, "requirements.txt")) as f:
        return [line.strip() for line in f.readlines() if line.strip()]


setup(
    name='dictmixin',
    version=re.search(
        r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
        open('dictmixin/__init__.py').read()).group(1),
    description='Parsing mixin which converts ``data class instance``, ``dict object``, ``json string`` and ``yaml string`` each other.',
    long_description=load_readme(),
    license='MIT',
    author='tadashi-aikawa',
    author_email='syou.maman@gmail.com',
    maintainer='tadashi-aikawa',
    maintainer_email='tadashi-aikawa',
    url='https://github.com/tadashi-aikawa/dictmixin.git',
    keywords='data class instance dict json yaml convert parse each other',
    packages=find_packages(exclude=['tests*']),
    install_requires=load_required_modules(),
    extras_require={
        'test': ['pytest', 'pytest-cov']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)

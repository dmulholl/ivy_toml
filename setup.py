#!/usr/bin/env python3
"""
TOML Metadata for Ivy
=====================

This Ivy plugin adds support for TOML file headers as an alternative to YAML.

"""

from setuptools import setup

setup(
    name = 'ivy_toml',
    version = '0.1.0',
    py_modules = ['ivy_toml'],
    install_requires = [
        'toml ~= 0.10',
    ],
    author = 'Darren Mulholland',
    url = 'https://github.com/dmulholl/ivy_toml',
    license = 'Public Domain',
    description = (
        'Adds TOML support to Ivy.'
    ),
    long_description = __doc__,
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: Public Domain',
    ],
)

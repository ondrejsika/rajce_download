#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'rajce_download',
    version = '1.0.0',
    download = 'http://github.com/sikaondrej/rajce_download',
    download_url = 'http://github.com/sikaondrej/rajce_download',
    license = 'MIT',
    description = 'Rajce.net photo downloader',
    author = 'Ondrej Sika',
    author_email = 'ondrej@ondrejsika.com',
    py_modules = [],
    scripts = ['rajce_download.py'],
    install_requires = ['requests', 'pyquery'],
)


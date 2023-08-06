#!/usr/bin/env python3

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ansiterm",
    version="1.0",
    author="Hiroyuki Ohsaki",
    author_email="ohsaki@lsnl.jp",
    description="a simple library to generate ANSI escape sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h-ohsaki/ansiterm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
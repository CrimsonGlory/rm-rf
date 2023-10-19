#!/usr/bin/env python
from setuptools import setup


description = ("Python 2 and 3 compatible POSIX rm -rf.")
long_description = ("See `github <https://github.com/CrimsonGlory/rm-rf>`_ "
                    "for more information.")

setup(
    name='rm-rf',
    version="0.1.0",
    description=description,
    long_description=long_description,
    author='CrimsonGlory',
    url='https://github.com/CrimsonGlory/rm-rf',
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    packages=[
        'rm_rf',
    ],
    package_dir={
        'rm_rf': 'rm_rf',
    },
)

#!/usr/bin/env python

from distutils.core import setup

setup(  name='ebupload',
        version='1.0',
        description='Simple uploader to ebu.io using the token api',
        author='Malik Bougacha',
        author_email='bougacha@ebu.ch',
        url='http://ebu.io',
        scripts=['bin/ebupload.py'],
        install_requires=['requests'],
    )

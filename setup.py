#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://pds3label.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pds3label',
    version='0.1.0',
    description='A Python module for parsing PDS3 labels.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Austin Godber',
    author_email='godber@uberhip.com',
    url='https://github.com/godber/pds3label',
    packages=[
        'pds3label',
    ],
    package_dir={'pds3label': 'pds3label'},
    include_package_data=True,
    install_requires=[
        'antlr4-python2-runtime==4.5',
        'antlr4-python3-runtime==4.5',
    ],
    license='MIT',
    zip_safe=False,
    keywords='pds3label',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

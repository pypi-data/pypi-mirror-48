#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_namespace_packages


VERSION = '0.0.1'
LONGDESC = '''
OrgCrawler Payloads
===================

A library of curated orgcrawler payload functions.

orgcrawler-payload is a sub-package within the OrgCrawler_ namespace.  See
the `Orgcrawler Readthedocs`_ page for full documentation of the OrgCrawler
suite of tools.


Installation
------------

::

  pip install orgcrawler-payload


Package Organization
--------------------

**orgcrawler.payload**
  The modules in ``orgcrawler.payload`` contain fully tested and supported
  payload functions divided accourding to AWS service

**orgcrawler.untested_payload**
  The modules in ``orgcrawler.untested_payload`` contain untested or
  experimental payload functions.  Many of these functions lack unittests only
  because the `Moto`_ library we use to mock AWS Services does not yet
  support a particular AWS API.  In time we expect to migrate them into the 
  ``orgcrawler.payload`` collection.

  **WARNING!!** These functions are **NOT** supported.  Use at your own risk.

.. _OrgCrawler: https://github.com/ucopacme/orgcrawler
.. _`OrgCrawler Readthedocs`: https://orgcrawler.readthedocs.io/en/latest/
.. _Moto: https://github.com/spulec/moto
'''

setup(
    name='orgcrawler.payload',
    version=VERSION,
    description='A library of orgcrawler payload functions',
    long_description=LONGDESC,
    long_description_content_type='text/x-rst',
    url='https://github.com/ucopacme/orgcrawler-payload',
    keywords='aws organizations boto3 orgcrawler',
    author='Ashley Gould - University of California Office of the President',
    author_email='agould@ucop.edu',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'botocore',
        'boto3',
        'orgcrawler',
    ],
    packages=find_namespace_packages(include=['orgcrawler.*']),
    zip_safe=False,

)

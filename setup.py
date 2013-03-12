#!/usr/bin/python

from setuptools import setup

setup(name='python-foreman-api',
      version='0.1',
      author='Stephan Adig',
      author_email='sh@sourcecode.de',
      description='A Foreman REST API Python Wrapper Library',
      license='LGPLv2', url='https://github.com/sadig/foreman-api',
      packages=[
        'foreman',
        'foreman.api',
        'foreman.factories'],
      install_requires=['restkit'],
      scripts=['scripts/foreman-cli.py']
      )

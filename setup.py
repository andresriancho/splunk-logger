#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname


setup(
      name='splunk_logger',

      version='0.1.4',
      license = 'GNU General Public License v2 (GPLv2)',
      platforms='Linux',
      
      description=('Splunk logger sends log messages to splunk directly from'
                   ' your Python code.'),
      long_description=open(join(dirname(__file__), 'README.rst')).read(),
      
      author='Andres Riancho',
      author_email='andres.riancho@gmail.com',
      url='https://github.com/andresriancho/splunk-logger/',
      
      packages=find_packages(),
      include_package_data=True,
      install_requires=['requests',],
      
      # https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring'
        ],
      
       # In order to run this command: python setup.py test
       test_suite="nose.collector",
       tests_require="nose",
     )

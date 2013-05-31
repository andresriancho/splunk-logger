Splunk logger
=============

A logging handler for Splunk. Lets you send information to Splunk directly from your Python code.

Usage
=====

::

	import logging
	from splunk_logger import SplunkLogger

	ACCESS_TOKEN = '...'
	PROJECT_ID = '...'

    splunk_logger = SplunkLogger(ACCESS_TOKEN, PROJECT_ID)
    logging.getLogger('').addHandler(splunk_logger)
    
    logging.info('This is sent to splunk')
    
Reporting bugs
==============

Report your issues and feature requests in `Splunk Logger's issue
tracker <https://github.com/andresriancho/splunk-logger/issues>`_ and I'll
be more than glad to fix them.


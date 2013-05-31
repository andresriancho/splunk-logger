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
    
    logging.error('This is sent to splunk')
    
After a couple of seconds of waiting for Splunk to process the new information,
you should be able to see something like this in the web interface:

::

    {
        data : "This is sent to splunk",
        level : "ERROR",
        line : 1,
        module : "<stdin>"
    }

When using the code in a real Python program, and not from the python console,
the real line number and module name are used.

Enhancements
============

There are a couple of things which could be improved in this module

 * python-requests module could be used in order to use HTTP's keep-alive and
   avoid creating a new TCP/IP connection for each message sent to Splunk
 * The logger could be refactored to send the messages in an async manner,
   this will make ``logging.foo()`` calls return immediately instead of waiting
   for the log message to be sent.  
 
Pull requests are more than welcome!

Reporting bugs
==============

Report your issues and feature requests in `Splunk Logger's issue
tracker <https://github.com/andresriancho/splunk-logger/issues>`_ and I'll
be more than glad to fix them.


Splunk logger
=============

A logging handler for Splunk. Lets you send information to Splunk directly from your Python code.

.. image:: https://circleci.com/gh/andresriancho/splunk-logger.png?circle-token=5f4c52c6972260273e0064a160dd9a503615a987
   :alt: Build Status
   :align: right
   :target: https://circleci.com/gh/andresriancho/splunk-logger
   
Usage
=====

Make sure you replace the ``***`` with your credentials and specific API domain
and run:

::

    import logging
    from splunk_logger import SplunkLogger
    
    ACCESS_TOKEN = '***'
    PROJECT_ID = '***'
    API_DOMAIN = 'api-***.data.splunkstorm.com'
    
    splunk_logger = SplunkLogger(access_token=ACCESS_TOKEN,
                                 project_id=PROJECT_ID,
                                 api_domain=API_DOMAIN)
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

Configuration file
==================

It is always a good idea to avoid hardcoded credentials in your source code.
The module can fetch the credentials from a YAML file in the current directory
or the user's home. The filename is named ``.splunk_logger`` and has the following
format:

::

    credentials:
        project_id: ***
        access_token: ***
        api_domain: api-***.data.splunkstorm.com

Once the file is in place, you can use the module as follows:

::

    import logging
    from splunk_logger import SplunkLogger

    # No credentials specified here
    splunk_logger = SplunkLogger()
    logging.getLogger('').addHandler(splunk_logger)
    
    logging.error('This is sent to splunk')


Configuration through environment variables
===========================================

Another configuration source accepted by splunk logger is environment variables.
Once again, you can use them to avoid hard-coding credentials in the source code:

* ``SPLUNK_PROJECT_ID``
* ``SPLUNK_ACCESS_TOKEN``
* ``SPLUNK_API_DOMAIN``

Enhancements
============

There are a couple of things which could be improved in this module

* The logger could be refactored to send the messages in an async manner,
  this will make ``logging.foo()`` calls return immediately instead of waiting
  for the log message to be sent.  
* Send messages in batches
 
Pull requests are more than welcome!

References
==========

This package implements communication with Storm Splunk as specified `here
<http://docs.splunk.com/Documentation/Storm/Storm/User/UseStormsRESTAPI>`_ .

Reporting bugs
==============

Report your issues and feature requests in `Splunk Logger's issue
tracker <https://github.com/andresriancho/splunk-logger/issues>`_ and I'll
be more than glad to fix them.

Change log
==========

* 30 Jun 2014: User needs to specify API endpoint domain. Fixes #2



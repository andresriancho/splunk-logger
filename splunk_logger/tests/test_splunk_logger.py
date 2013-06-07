import os
import unittest
import logging

from mock import patch

from splunk_logger import SplunkLogger
from splunk_logger.utils import _parse_config_file_impl

CONFIG_ERROR = '''\
The file .splunk_logger with correct credentials is required to run the unittests.
'''


class TestSplunkLogger(unittest.TestCase):
    '''
    Sadly I have no way of knowing if the message really made it to Splunk
    since there is no API for searching in splunk storm. To verify that things
    work, just browse to the corresponding project.
    '''
    
    def test_send_incorrect_credentials(self):
        ACCESS_TOKEN = 'foo'
        PROJECT_ID = 'bar'
        
        splunk_logger = SplunkLogger(access_token=ACCESS_TOKEN, project_id=PROJECT_ID)
        root = logging.getLogger('')
        root.addHandler(splunk_logger)
        
        devnull = open(os.devnull, 'w')
        with patch('sys.stderr', devnull):
            logging.error('This is NOT sent to splunk')
        
        root.handlers.remove(splunk_logger)
    
    def test_send_credentials_from_file(self):
        self.assertTrue(os.path.exists('.splunk_logger'), CONFIG_ERROR)
         
        # Get credentials from file
        splunk_logger = SplunkLogger()
        root = logging.getLogger('')
        root.addHandler(splunk_logger)
        
        logging.info('This was sent to splunk with credentials from file')

        root.handlers.remove(splunk_logger)
    
    def test_send_credentials_from_params(self):
        self.assertTrue(os.path.exists('.splunk_logger'), CONFIG_ERROR)
         
        # Get credentials from file and pass them as params
        project_id, access_token = _parse_config_file_impl('.splunk_logger')
        splunk_logger = SplunkLogger(access_token=access_token, project_id=project_id)
        root = logging.getLogger('')
        root.addHandler(splunk_logger)
        
        logging.info('This was sent to splunk with credentials from params')
        
        root.handlers.remove(splunk_logger)

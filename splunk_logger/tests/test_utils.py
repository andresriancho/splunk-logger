import unittest
import tempfile
import os

from splunk_logger.utils import _parse_config_file_impl


CONFIG_FMT = '''\
credentials:
    project_id: %s
    access_token: %s
    api_domain: %s
'''


class TestParseConfigFile(unittest.TestCase):
    def test_parse_config_ok(self):
        
        PROJECT_ID = 'abc'
        ACCESS_TOKEN = 'def/123'
        API_DOMAIN = 'foo.com'
        
        fh = tempfile.NamedTemporaryFile('w', delete=False)
        fh.write(CONFIG_FMT % (PROJECT_ID, ACCESS_TOKEN, API_DOMAIN))
        fh.close()
        
        project_id, access_token, api_domain = _parse_config_file_impl(fh.name)
        self.assertEqual(project_id, PROJECT_ID)
        self.assertEqual(access_token, ACCESS_TOKEN)
        self.assertEqual(api_domain, API_DOMAIN)
        
        os.unlink(fh.name)

    def test_parse_config_not_exists(self):
        project_id, access_token, api_domain = _parse_config_file_impl('/bar')
        self.assertEqual(project_id, None)
        self.assertEqual(access_token, None)
        self.assertEqual(api_domain, None)
    
    def test_parse_config_invalid_format(self):
        fh = tempfile.NamedTemporaryFile('w', delete=False)
        fh.write('hello world!')
        
        project_id, access_token, api_domain = _parse_config_file_impl(fh.name)
        self.assertEqual(project_id, None)
        self.assertEqual(access_token, None)
        self.assertEqual(api_domain, None)

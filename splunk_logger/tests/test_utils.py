import unittest
import tempfile
import os

from splunk_logger.utils import _parse_config_file_impl


CONFIG_FMT = '''\
credentials:
    project_id: %s
    access_token: %s
'''

class TestParseConfigFile(unittest.TestCase):
    def test_parse_config_ok(self):
        
        PROJECT_ID = 'abc'
        ACCESS_TOKEN = 'def/123'
        
        fh = tempfile.NamedTemporaryFile('w', delete=False)
        fh.write(CONFIG_FMT % (PROJECT_ID, ACCESS_TOKEN))
        fh.close()
        
        project_id, access_token = _parse_config_file_impl(fh.name)
        self.assertEqual(project_id, PROJECT_ID)
        self.assertEqual(access_token, ACCESS_TOKEN)
        
        os.unlink(fh.name)

    def test_parse_config_not_exists(self):
        project_id, access_token = _parse_config_file_impl('/foo/bar')
        self.assertEqual(project_id, None)
        self.assertEqual(access_token, None)
    
    def test_parse_config_invalid_format(self):
        fh = tempfile.NamedTemporaryFile('w', delete=False)
        fh.write('hello world!')
        
        project_id, access_token = _parse_config_file_impl(fh.name)
        self.assertEqual(project_id, None)
        self.assertEqual(access_token, None)

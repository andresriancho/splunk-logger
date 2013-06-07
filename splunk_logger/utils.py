import os
import yaml


def parse_config_file():
    '''
    Find the .splunk_logger config file in the current directory, or in the
    user's home and parse it. The one in the current directory has precedence.
    
    :return: A tuple with:
                - project_id
                - access_token
    '''
    for filename in ('.splunk_logger', os.path.expanduser('~/.splunk_logger')):
        project_id, access_token = _parse_config_file_impl(filename)
        if project_id is not None and access_token is not None: 
            return project_id, access_token
    else:
        return None, None
       
def _parse_config_file_impl(filename):
    '''
    Format for the file is:
    
         credentials:
             project_id: ...
             access_token: ...
    
    :param filename: The filename to parse
    :return: A tuple with:
                - project_id
                - access_token
    '''
    try:
        doc = yaml.load(file(filename).read())
        
        project_id = doc["credentials"]["project_id"]
        access_token = doc["credentials"]["access_token"]
        
        return project_id, access_token
    except:
        return None, None
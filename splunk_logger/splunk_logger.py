import urllib
import urllib2
import socket
import json
import base64
import logging
import gzip
import cStringIO


class SplunkLogger(logging.Handler):
    """
    A class to send messages to splunk storm using their API
    """

    def __init__(self, access_token, project_id, input_url=None):
        logging.Handler.__init__(self)
        
        self.url = input_url or 'https://api.splunkstorm.com/1/inputs/http'
        self.project_id = project_id
        self.access_token = access_token

        raw_values = "%s:%s" % ('x', access_token)
        auth = 'Basic %s' % base64.b64encode(raw_values).strip()

        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('Authorization', auth), ('Content-Encoding', 'gzip')]

    def usesTime(self):
        return False

    def _compress(self, input_str):
        
        compressed_bits = cStringIO.StringIO()
        
        f = gzip.GzipFile(fileobj=compressed_bits, mode='wb')
        f.write(input_str)
        f.close()
        
        return compressed_bits.getvalue()

    def emit(self, record):
        try:
            self._send_to_splunk(record)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
            
    def _send_to_splunk(self, record):
        # http://docs.splunk.com/Documentation/Storm/latest/User/Sourcesandsourcetypes
        sourcetype = 'json_no_timestamp'
        
        host = socket.gethostname()
        
        event_dict = {'data': self.format(record),
                      'level': record.levelname,
                      'module': record.module,
                      'line': record.lineno}
        event = json.dumps(event_dict)
        event = self._compress(event)
        
        params = {'project': self.project_id,
                  'sourcetype': sourcetype}
        params['host'] = host

        url = '%s?%s' % (self.url, urllib.urlencode(params))
        req = urllib2.Request(url, event)
        response = self.opener.open(req)
        body = response.read()
        return body


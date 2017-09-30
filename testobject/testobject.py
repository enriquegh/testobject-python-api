
import httplib2
import base64
import logging
import logging.config
import yaml
import json

from .devices import Devices

logger = logging.getLogger(__name__)

class TestObject(object):

	URL_BASE = "https://app.testobject.com/api/rest"


	def __init__(self, username, api_key):

		self.username = username
		self.api_key = api_key
		self.devices = Devices(self)

	def request(self, method, endpoint):

		url = TestObject.URL_BASE + endpoint
		logger.info("URL: %s",url)
		http_conn = httplib2.Http()
		http_conn.add_credentials(self.username, self.api_key)

		response_info, content = http_conn.request(url, method=method)

		#vcrpy sends requests as a bytestring and this is not allowed as a parameter on json on python 3
		content = content.decode('utf-8') 
		content_json = json.loads(content)

		logger.info("response: %s",response_info)
		logger.debug("content: %s", content_json)

		return content_json
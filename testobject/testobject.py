
import httplib2
import base64
import logging
import logging.config
import yaml

logger = logging.getLogger(__name__)

class TestObject(object):

	URL_BASE = "https://app.testobject.com/api/rest"


	def __init__(self, username, api_key):

		self.username = username
		self.api_key = api_key

	def request(self, method, endpoint):

		url = TestObject.URL_BASE + endpoint
		logger.info("URL: %s",url)
		http_conn = httplib2.Http()
		http_conn.add_credentials(self.username, self.api_key)

		response, content = http_conn.request(url, method=method)

		logger.info("response: %s",response)
		logger.debug("content: %s", content)

		return content

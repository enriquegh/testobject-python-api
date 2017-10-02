
import base64
import logging
import logging.config
import yaml
import json
import requests

from .devices import Devices
from .suites import Suites

logger = logging.getLogger(__name__)

class TestObject(object):

	URL_BASE = "https://app.testobject.com/api/rest"


	def __init__(self, username, api_key):

		self.username = username
		self.api_key = api_key
		self.devices = Devices(self)
		self.suites = Suites(self)

	def request(self, method, endpoint, auth_type=None, data=None):
		url = TestObject.URL_BASE + endpoint
		logger.info("URL: %s",url)

		content = None

		#Appium Suites API needs a different authentication
		# "All endpoints in Appium Suites API require basic authentication with
		# the API Key as the username and the password left blank."
		if auth_type == 'suite':
			content = requests.request(method, url, auth=(self.api_key, ''), json=data)
		else:
			content = requests.request(method, url, auth=(self.username, self.api_key), json=data)

		logger.debug("content: %s", content)

		return json.loads(content.text)

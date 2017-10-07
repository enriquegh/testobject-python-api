
import base64
import logging
import logging.config
import yaml
import json
import requests

from testobject.devices import Devices
from testobject.suites import Suites
from testobject.watcher import Watcher

logger = logging.getLogger(__name__)

class TestObject(object):

	URL_BASE = "https://app.testobject.com/api/rest"


	def __init__(self, username, api_key):

		self.username = username
		self.api_key = api_key
		self.devices = Devices(self)
		self.suites = Suites(self)
		self.watcher = Watcher(self)

	def request(self, method, endpoint, auth_type=None, data=None):
		url = TestObject.URL_BASE + endpoint
		logger.info("URL: %s",url)

		auth = None

		#Appium Suites API needs a different authentication
		# "All endpoints in Appium Suites API require basic authentication with
		# the API Key as the username and the password left blank."
		# Watcher API needs no authentication
		if auth_type == 'suite':
			auth=(self.api_key, '')
		elif auth_type == 'watcher':
			pass
		else:
			auth=(self.username, self.api_key)

		content = requests.request(method, url, auth=auth, json=data)

		logger.debug("content: %s", content)

		return content

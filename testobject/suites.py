

class Suites(object):

	def __init__(self, testobject):
		self.testobject = testobject

	def update_suite(self, batch_id):
		method = 'PUT'
		endpoint = '/v2/appium/suites/{batch_id}'.format(batch_id=batch_id)

		content = self.testobject.request(method, endpoint)

		return content

	def get_devices_ids(self, batch_id):
		method = 'GET'
		endpoint = '/v2/appium/suites/{batch_id}/deviceIds'.format(batch_id=batch_id)

		content = self.testobject.request(method, endpoint, auth_type='suite')

		return content

	def start_suite(self, batch_id):
		method = 'POST'
		endpoint = '/v2/appium/{batch_id}/reports/start'.format(batch_id=batch_id)

		content = self.testobject.request(method, endpoint, auth_type='suite')

		return content

	def stop_suite(self, batch_id, batch_report_id):
		pass
 
	def stop_suite_test(self, batch_id, batch_report_id, test_report_id):
		pass

	def skip_suite_test(self, batch_id, batch_report_id, test_report_id):
		pass


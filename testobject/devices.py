

class Devices(object):

    def __init__(self, testobject):
        self.testobject = testobject

    def get_devices(self):
        method = 'GET'
        endpoint = '/v2/devices'

        content = self.testobject.request(method, endpoint)

        return content

    def get_available_devices(self):
        method = 'GET'
        endpoint = '/v2/devices/available'

        content = self.testobject.request(method, endpoint)

        return content

    def get_device(self, descriptor_id):
        method = 'GET'
        endpoint = '/v2/devices/{}'.format(descriptor_id)

        content = self.testobject.request(method, endpoint)

        return content

    def get_session_reports(self, last_days=None, offset=None, limit=None):
        method = 'GET'
        endpoint = '/v1/devices/reports'

        content = self.testobject.request(method, endpoint)
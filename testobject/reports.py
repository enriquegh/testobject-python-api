class Reports(object):

    def __init__(self, testobject):
        self.testobject = testobject

    def get_test_report(self, test_report_id):
        method = 'GET'
        endpoint = '/v2/reports/{test_report_id}'.format(test_report_id=test_report_id)

        response = self.testobject.request(method, endpoint)

        return response
    
    def get_screenshot(self, test_report_id, screenshot_id):
        pass

    def get_video(self, video_id):
        pass
    
    def get_appium_log(self, test_report_id):
        pass

    def get_device_log(self, test_report_id):
        pass

    def get_vitals_log(self, test_report_id):
        pass

    def get_xcuitest_log(self, test_report_id):
        pass
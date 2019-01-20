import vcr
import os
import pytest
import uuid

from testobject.client import TestObject
from testobject.client import NoPasswordException

from .keys import *

UPLOAD_APP_PATH = os.environ.get('UPLOAD_APP_PATH',"./README.md")

@pytest.fixture
def to():
    username = os.environ.get('TO_USERNAME', None)
    api_key = os.environ.get('TO_API_KEY', None)
    password = os.environ.get('TO_PASSWORD', None)

    return TestObject(username, api_key, password)

@vcr.use_cassette('tests/vcr_cassettes/all-devices.yml', filter_headers=['authorization'])
def test_get_devices(to):

    response = to.devices.get_devices()
    datacenters = response.json()

    assert datacenters, dict

    for _, datacenter in datacenters.items():
        for device in datacenter:
            assert EXPECTED_DEVICE_KEYS.issubset(device)


@vcr.use_cassette('tests/vcr_cassettes/available-devices.yml', filter_headers=['authorization'])
def test_get_available_devices(to):

    response = to.devices.get_available_devices()

    datacenters = response.json()

    assert datacenters, dict


@vcr.use_cassette('tests/vcr_cassettes/device.yml', filter_headers=['authorization'])
def test_get_device(to):

    device_name = 'iPhone_5_free'

    response = to.devices.get_device(device_name)

    datacenters = response.json()

    assert datacenters, dict
    assert datacenters['US']['id'] == device_name
    for _, device in datacenters.items():
        assert EXPECTED_DEVICE_KEYS.issubset(device)


@vcr.use_cassette('tests/vcr_cassettes/get-session-reports.yml', filter_headers=['authorization'])
def test_session_reports(to):
    with pytest.raises(NoPasswordException):
        response = to.devices.get_session_reports()
        reports = response.json()

        assert reports, dict
        assert EXPECTED_SESSION_REPORT_KEYS.issubset(reports)
        for key in reports['entities']:
            assert EXPECTED_SESSION_REPORT_ENTITIY_KEYS.issubset(key)
        to.password = None
        response = to.devices.get_session_reports()


@vcr.use_cassette('tests/vcr_cassettes/get-device-ids.yml', filter_headers=['authorization'])
def test_get_devices_ids(to):

    response = to.suites.get_devices_ids(14)
    content = response.json()
    assert content, dict
    for keys in content:
        assert EXPECTED_SUITE_DEVICES_KEYS.issubset(keys)

@vcr.use_cassette('tests/vcr_cassettes/update-suite.yml', filter_headers=['authorization'])
def test_update_suite(to):
    data = {}
    data['title'] = "MY NAME CHANGING SUITE"


    response = to.suites.update_suite(14, data)
    content = response.json()
    assert content, dict
    assert EXPECTED_SUITE_KEYS.issubset(content)

@vcr.use_cassette('tests/vcr_cassettes/start-suite.yml', filter_headers=['authorization'])
def test_start_suite(to):
    report = {'className': 'TOSuiteTest', 'dataCenterId': 'US', 'methodName': 'testMethod', 'deviceId': 'iPhone_5_free'}
    data = [report]

    response = to.suites.start_suite(14, data)
    content = response.json()

    assert content, dict
    EXPECTED_START_SUITE_KEYS.issubset(content)
    for tests in content['testReports']:
        assert EXPECTED_TEST_REPORT_KEYS.issubset(tests)
        assert EXPECTED_TEST_KEYS.issubset(tests['test'])


@vcr.use_cassette('tests/vcr_cassettes/stop-suite.yml', filter_headers=['authorization'])
def test_stop_suite(to):

    response = to.suites.stop_suite(14, 17)
    content = response.json()

    assert content, dict
    EXPECTED_START_SUITE_KEYS.issubset(content)
    for tests in content['testReports']:
        assert EXPECTED_TEST_REPORT_KEYS.issubset(tests)
        assert EXPECTED_TEST_KEYS.issubset(tests['test'])

@vcr.use_cassette('tests/vcr_cassettes/stop-suite-test.yml', filter_headers=['authorization'])
def test_stop_suite_test(to):

    response = to.suites.stop_suite_test(14, 17, 63, True)
    content = response.json()

    assert content, dict
    assert EXPECTED_TEST_REPORT_KEYS.issubset(content)
    assert EXPECTED_TEST_KEYS.issubset(content['test'])


@vcr.use_cassette('tests/vcr_cassettes/skip-suite-test.yml', filter_headers=['authorization'])
def test_skip_test(to):

    response = to.suites.skip_suite_test(14, 11, 55)
    content = response.json()

    assert content, dict
    assert EXPECTED_TEST_REPORT_KEYS.issubset(content)
    assert EXPECTED_TEST_KEYS.issubset(content['test'])

@vcr.use_cassette('tests/vcr_cassettes/skip-test-report.yml', filter_headers=['authorization'])
def test_skip_test_report(to):

    response = to.watcher.skip_test_report('95ffffe9-4eb0-418e-87d0-4f1d59fa19fe')

    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/report-test-result.yml', filter_headers=['authorization'])
def test_report_test_result(to):
    response = to.watcher.report_test_result('95ffffe9-4eb0-418e-87d0-4f1d59fa19fe', False)

    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/upload_app.yml', filter_headers=['authorization'])
def test_upload_app(to):
    display_name = str(uuid.uuid4())

    response = to.storage.upload_app(UPLOAD_APP_PATH, display_name, False)

    content = response.text

    assert content, str
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/upload_app.yml', filter_headers=['authorization','App-DisplayName'])
def test_upload_app_no_display_name(to):

    response = to.storage.upload_app(UPLOAD_APP_PATH, None, False)

    content = response.text

    assert content, str
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_test_report.yml', filter_headers=['authorization'])
def test_get_test_report(to):

    response = to.reports.get_test_report(4)
    content = response.json()

    assert content, dict
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_screenshot.yml', filter_headers=['authorization'])
def test_get_screenshot(to):

    response = to.reports.get_screenshot(4, 1)

    assert response.content, bytes 
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_video.yml', filter_headers=['authorization'])
def test_get_video(to):

    response = to.reports.get_video('8f1aac1e-5434-47e7-bb7b-81cc89436327')

    assert response.content, bytes
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_appium_log.yml', filter_headers=['authorization'])
def test_get_appium_log(to):
    
    response = to.reports.get_appium_log('4')
    content = response.json()

    assert content, list
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_device_log.yml', filter_headers=['authorization'])
def test_get_device_log(to):
    
    response = to.reports.get_device_log('4')
    content = response.json()

    assert content, list
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_vitals_log.yml', filter_headers=['authorization'])
def test_get_vitals_log(to):
    
    response = to.reports.get_vitals_log('6')
    content = response.text

    assert content, str
    assert response.ok

@vcr.use_cassette('tests/vcr_cassettes/get_xcuitest_log.yml', filter_headers=['authorization'])
def test_get_xcuitest_log(to):

    response = to.reports.get_xcuitest_log('3')
    content = response.text

    assert content, list
    assert response.ok

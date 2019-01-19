import vcr
import os
import pytest
import uuid

from testobject.client import TestObject
from testobject.client import NoPasswordException

EXPECTED_DEVICE_KEYS = set([
    'internalStorageSize', 
    'isArm', 
    'ramSize', 
    'isKeyGuardDisabled', 
    'isTablet', 
    'defaultOrientation', 
    'supportsXcuiTest', 
    'resolutionWidth', 
    'apiLevel', 
    'id', 
    'isAlternativeIoEnabled', 
    'cpuFrequency', 
    'resolutionHeight', 
    'hasHardwareKeyboard', 
    'supportsMockLocations', 
    'isPrivate', 
    'dpiName', 
    'isRooted', 
    'abiType', 
    'supportsAppiumWebAppTesting', 
    'sdCardSize', 
    'osVersion', 
    'manufacturer', 
    'hasOnScreenButtons', 
    'name', 
    'cpuCores', 
    'pixelsPerPoint', 
    'modelNumber', 
    'screenSize', 
    'supportsManualWebTesting', 
    'deviceFamily', 
    'os', 
    'dpi'

])
EXPECTED_SUITE_DEVICES_KEYS = set([
    'dataCenterId',
    'dataCenterURL',
    'deviceDescriptorIds'

])
EXPECTED_SUITE_KEYS = set([
    'id',
    'title',
    'appVersionId',
    'frameworkVersion',
    'deviceIds'
])

EXPECTED_START_SUITE_KEYS = set([
    'id',
    'testReports'

])

EXPECTED_TEST_REPORT_KEYS = set([
    'id',
    'test'

])

EXPECTED_SESSION_REPORT_KEYS = set([
    'entities',
    'metaData'
])

EXPECTED_SESSION_REPORT_ENTITIY_KEYS = set([
    'id',
    'projectId',
    'userId',
    'deviceDescriptorId',
    'usage',
    'appId',
    'frameworkAppId',
    'testFrameworkType',
    'testFrameworkVersion',
    'testReportIds',
    'testIds',
    'batchId',
    'startDateTime',
    'endDateTime',
    'durationInSeconds'

])

EXPECTED_TEST_KEYS = set([
    'className',
    'methodName',
    'deviceId',
    'dataCenterId'

])

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
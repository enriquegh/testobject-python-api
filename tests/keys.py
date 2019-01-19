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

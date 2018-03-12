# testobject-python-api

[![Build Status](https://travis-ci.org/enriquegh/testobject-python-api.svg?branch=master)](https://travis-ci.org/enriquegh/testobject-python-api) [![codecov](https://codecov.io/gh/enriquegh/testobject-python-api/branch/master/graph/badge.svg)](https://codecov.io/gh/enriquegh/testobject-python-api) [![PyPI version](https://badge.fury.io/py/testobject.svg)](https://badge.fury.io/py/testobject)

A Python library client for TestObject API

For more on the API you can visit TestObject's docs [here](https://api.testobject.com/).

## Getting Started

### Installing

To install on your machine run:
```bash
pip install testobject
```

Once installed you can run something like:
```python
import testobject
client = testobject.TestObject('myusername','my_api_key', password='password')
# Password only needed if using Session Reports
response = client.devices.get_devices()
devices = response.json()
us_devices = devices['US']
```


## Running the tests

Tests are done with pytest.
To run these simply run:
```bash
pytest
```

## Docs

### Get All Devices

```python
response = client.devices.get_devices()
devices = response.json()
us_devices = devices['US']
```

### Get Available Devices

```python
response = client.devices.get_available_devices()
devices = response.json()
us_devices = devices['US']
```

### Get Device

```python
response = client.devices.get_device('iPhone_5_free')
device = response.json()
```

### Get Session Reports
```python
response = client.devices.get_session_reports(last_days=30, offset=1, limit=50)
reports = response.json()
```

### Update Appium Suite

```python
data = {}
data['title'] = "New Suite Title"
response = client.suites.update_suite(suite_number,data)
content = response.json()
```

### Start Appium Suite Report

```python
report = {'className': 'TOTestClass', 'dataCenterId': 'US', 'methodName': 'testMethod', 'deviceId': 'iPhone_5_free'}
data = [report] # If more than one test and/or class add more reports to the data list
response = to.suites.start_suite(suite_number, data)
content = response.json()
```

### Stop Appium Suite Report

```python
response = to.suites.stop_suite(suite_number, suite_report_number)
content = response.json()
```

### Stop Appium Suite Test

```python
response = to.suites.stop_suite_test(suite_number, suite_report_number, suite_test_number, True)
content = response.json()
```

### Skip Appium Suite Test

```python
response = to.suites.stop_suite_test(suite_number, suite_report_number, suite_test_number)
content = response.json()
```

### Skip Appium Test Report

```python
response = to.watcher.skip_test_report('appium_session_id')
```

### Send Appium Test Report

```python
response = to.watcher.skip_test_report('appium_session_id',True)
```

## Authors

* **Enrique Gonzalez** - *Maintainer* - [enriquegh](https://github.com/enriquegh)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

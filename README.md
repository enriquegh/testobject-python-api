# testobject-python-api

[![Build Status](https://travis-ci.org/enriquegh/testobject-python-api.svg?branch=master)](https://travis-ci.org/enriquegh/testobject-python-api) [![codecov](https://codecov.io/gh/enriquegh/testobject-python-api/branch/master/graph/badge.svg)](https://codecov.io/gh/enriquegh/testobject-python-api)

A Python library client for TestObject API

For more on the API you can visit TestObject's docs [here](https://api.testobject.com/).

## Getting Started

### Installing

This package is not released on PyPi yet so for now you need to download and use manually.

Clone repository

```bash
git clone https://github.com/enriquegh/testobject-python-api
```

Change directory to the the root of the repo

```bash
cd testobject-python-api
```

Once installed you can run something like:
```python
import testobject
client = testobject.TestObject('myusername','my_api_key')
response = client.devices.get_devices()
devices = response.json.get('US')
```


## Running the tests

Tests are done with pytest.
To run these simply run:
```bash
pytest
```


## Authors

* **Enrique Gonzalez** - *Maintainer* - [enriquegh](https://github.com/enriquegh)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

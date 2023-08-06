# Dyspatch Python Client
# Introduction  
The Dyspatch API is based on the REST paradigm, and features resource based URLs with standard HTTP response codes to indicate errors. We use standard HTTP authentication and request verbs, and all responses are JSON formatted. 
## API Client Libraries  
Dyspatch provides API Clients for popular languages and web frameworks.   
- [Java](https://github.com/getdyspatch/dyspatch-java) 
- [Javascript](https://github.com/getdyspatch/dyspatch-javascript) 
- [Python](https://github.com/getdyspatch/dyspatch-python) 
- [C#](https://github.com/getdyspatch/dyspatch-dotnet) 
- [Go](https://github.com/getdyspatch/dyspatch-golang) 
- [Ruby](https://github.com/getdyspatch/dyspatch-ruby) 

- API version: 2019.03
- Package version: 2.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

For more information, please visit [https://docs.dyspatch.io](https://docs.dyspatch.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install dyspatch-python
```

Then import the package:
```python
import dyspatch_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dyspatch_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import dyspatch_client
from dyspatch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = dyspatch_client.Configuration()
configuration.api_key['Authorization'] = 'Dyspatch_API_key'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dyspatch_client.TemplatesApi(dyspatch_client.ApiClient(configuration))
cursor = 'example_cursor' # str | A cursor value used to retrieve a specific page from a paginated result set. (optional)

try:
    # List Templates
    api_response = api_instance.templates_get(cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.dyspatch.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LocalizationsApi* | [**localizations_localization_id_get**](docs/LocalizationsApi.md#localizations_localization_id_get) | **GET** /localizations/{localizationId} | Get Localization Object by ID
*TemplatesApi* | [**templates_get**](docs/TemplatesApi.md#templates_get) | **GET** /templates | List Templates
*TemplatesApi* | [**templates_template_id_get**](docs/TemplatesApi.md#templates_template_id_get) | **GET** /templates/{templateId} | Get Template by ID

## Documentation For Models

 - [APIError](docs/APIError.md)
 - [CompiledRead](docs/CompiledRead.md)
 - [Cursor](docs/Cursor.md)
 - [LocalizationMetaRead](docs/LocalizationMetaRead.md)
 - [LocalizationRead](docs/LocalizationRead.md)
 - [TemplateMetaRead](docs/TemplateMetaRead.md)
 - [TemplateRead](docs/TemplateRead.md)
 - [TemplatesRead](docs/TemplatesRead.md)

## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@dyspatch.io

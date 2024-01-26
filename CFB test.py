from __future__ import print_function
import config
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
import pandas as pd

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = config.api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = cfbd.PlaysApi(cfbd.ApiClient(configuration))
api_response = api_instance.get_plays(year=2023, week=10)
print(api_response)
print(len(api_response))
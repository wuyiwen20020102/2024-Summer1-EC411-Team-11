import json
from tripadvisorapi.api import TripadvisorApi

key = '3265045EBF3847FCB2DCB6213C1FE9EB'
api = TripadvisorApi(key)
res = api.location_search("Los Angeles")
res_json = json.loads(res.text)
print(res_json)

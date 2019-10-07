
import json
import requests

api_url = 'http://127.0.0.1:5000/api/recommend'
row_data = {'interest':'Biosphere'}
r = requests.post(url=api_url, json=row_data)
print(r.status_code,r.reason)

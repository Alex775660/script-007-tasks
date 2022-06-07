import requests
import json
def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)


response = requests.post('http://127.0.0.1:80/change_dir/', data=to_json({'path': 'user/data'}))
print(f'code: {response.status_code}')
print(f'body: {response.text}')

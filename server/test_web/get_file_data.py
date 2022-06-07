import requests
import json
def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)

response = requests.get('http://127.0.0.1:80/get_file_data/?filename="poem.txt"')
print(f'code: {response.status_code}')
# print(f'body: {response.text}')
pretty_response = to_json(json.loads(response.text))
print(f'body: {pretty_response}')

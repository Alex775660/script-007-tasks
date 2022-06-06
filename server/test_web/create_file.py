import requests
import json
def to_json(obj):
    return json.dumps(obj, indent=2, sort_keys=True)

response = requests.post('http://127.0.0.1:80/create_file/', data=to_json({
    'filename': 'poem.txt',
    'content': 'New file content\r\nIn two lines!',
}))
print(f'code: {response.status_code}')
print(f'body: {response.text}')

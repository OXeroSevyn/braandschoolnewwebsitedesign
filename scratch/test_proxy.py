import urllib.request
import urllib.error
import json

url = 'http://localhost:8000/api/submit'
payload = {
    'embeds': [{
        'title': 'Test from Local Proxy',
        'description': 'It works!'
    }]
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)

try:
    response = urllib.request.urlopen(req)
    print("Success:", response.read().decode())
except urllib.error.HTTPError as e:
    print("Error Code:", e.code)
    print("Error Body:", e.read().decode())
except Exception as e:
    print("Other Exception:", str(e))

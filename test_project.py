import requests


url = 'http://httpbin.org/status/200'
r = requests.get(url)

if 'json' in r.headers.get('Content-Type'):
    js = r.json()
else:
    print('Response content is not in JSON format.')
    js = 'spam'
import requests


url = 'https://github.com/'
r = requests.get(url)

if 'json' in r.headers.get('Content-Type'):
    js = r.json()
elif 'text' in r.headers.get('Content-Type'):
	print('Response is in text/html format')
else:
    print('Response content is not in JSON format.')
    js = 'spam'
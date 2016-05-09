import json
import requests
#import urllib.request

with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']

r = requests.get('https://freemusicarchive.org/featured.json', 
                 data={'api_key': API_KEY})

# f = urllib.request.urlopen('http://freemusicarchive.org/featured.json')
# print(f.read(100).decode('utf-8'))
x = r.json()

print(r.url)
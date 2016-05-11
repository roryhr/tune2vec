import json
import requests
from pathlib import Path

with open('api_key.json') as f:
    API_KEY = json.load(f)['API_KEY']

# Get 300 featured tracks
r = requests.get('https://freemusicarchive.org/featured.json',
                 data={'api_key': API_KEY})
tracks = r.json()['aTracks']

for track in tracks[:90]:
    file_path = Path(track['track_file'])
    if file_path.exists():
        continue

    print(file_path)
    try:
        file_path.parent.mkdir(parents=True)
    except FileExistsError:
        pass

    r2 = requests.get(track['track_file_url'],
                      params={'api_key': API_KEY})

    with open(str(file_path), mode='wb') as f:
        f.write(r2.content)

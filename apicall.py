import json
import requests
import sys
import spotipy
import spotipy.util as util
client_id='c0d2821e26fd468db7d04420ef7e0554'
client_secret='cf5d6bfebe414d659eaefebf54e79682'
scope = 'playlist-modify-public'
redirect_uri='http://127.0.0.1:8000/'
username="xxxxxx"
api_token = util.prompt_for_user_token(username, scope,client_id,client_secret,redirect_uri)
api_url_base = 'https://api.spotify.com/v1/playlists/'
playlist_link='https://open.spotify.com/playlist/4eHCyJ3tMT4m4oaMHJ3b9E?si=IUJx1HxwQKKif5TRtXcRtw'
l=playlist_link.split('/')[4].split('?')[0]
if api_token:
    print("here",api_token)
    headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
    api_url = api_url_base+l
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        playlist=json.loads(response.content.decode('utf-8'))
        print(playlist['owner']['id'])
        print(playlist['name'])
        print(playlist['images'][0]['url'])

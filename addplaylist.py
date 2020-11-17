import sys
import spotipy
import spotipy.util as util
client_id='c0d2821e26fd468db7d04420ef7e0554'
client_secret='cf5d6bfebe414d659eaefebf54e79682'
scope = 'playlist-modify-public'
redirect_uri='http://127.0.0.1:8000/'
username="mysvp8pmzgzzpp0fiol1tt4ow"
token = util.prompt_for_user_token(username, scope,client_id,client_secret,redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.user_playlist_follow_playlist('fp6k8tq9ng4ykw1qzqcvbw3gy','4eHCyJ3tMT4m4oaMHJ3b9E')

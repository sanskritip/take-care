from django.contrib import admin
from .models import Playlist,Spotify_user


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('name','author','playlist_id', 'owner_id','created_on')
    search_fields = ['name']
admin.site.register(Playlist,PlaylistAdmin)
admin.site.register(Spotify_user)
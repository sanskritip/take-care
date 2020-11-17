from .models import Playlist
from django import forms

class AddPlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ('link')

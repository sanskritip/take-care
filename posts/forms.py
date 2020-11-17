from .models import Picture, PComment
from django import forms


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('title', 'image','caption')


class CommentForm(forms.ModelForm):
    class Meta:
        model = PComment
        fields = ('body',)

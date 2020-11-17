from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Playlist(models.Model):

    name = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='playlist_author')
    updated_on = models.DateTimeField(auto_now= True)
    link = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    cover_url=models.TextField()
    playlist_id=models.CharField(max_length=500)
    owner_id=models.CharField(max_length=500)
    class Meta:
        ordering = ['-created_on']
    def save(self,*args,**kwargs):
        super(Post,self).save(*args,**kwargs)

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Tag(models.Model):
    name = models.CharField(max_length =20)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True,null=True)
    content_object = GenericForeignKey('content_type')
    def __str__(self):
        return '{} has tag {}'.format(self.content_object,self.name)

class Follow(models.Model):
    user_from = models.ForeignKey(User,on_delete=models.CASCADE ,related_name = "follow_ing")
    user_to = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="follow_er")
    created = models.DateTimeField(auto_now_add = True,db_index = True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "{} follows {}".format(self.user_from,self.user_to)

class Like(models.Model):
    liked_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='like')
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True,null=True)
    content_object = GenericForeignKey('content_type')

    def __str__(self):
        return '{} liked {}'.format(self.liked_by,self.content_object)
class Saves(models.Model):
    saved_by = models.ForeignKey(User, on_delete= models.CASCADE,related_name='saves')
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True,null=True)
    content_object = GenericForeignKey('content_type')

    def __str__(self):
        return '{} saved {}'.format(self.saved_by,self.content_object)


# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from feed.models import Like,Tag,Saves
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = GenericRelation(Like,related_query_name="post_likes")
    saves= GenericRelation(Saves,related_query_name="post_saves")
    tagname = models.CharField(max_length=30, default = "post")
    tag = GenericRelation(Tag,related_query_name="tags")

    class Meta:
        ordering = ['-created_on']
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    #name = models.CharField(max_length=80)
    #email = models.EmailField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)

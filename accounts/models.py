from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Bio(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE,related_name='bio_user')
    firstname = models.CharField(max_length=100, unique=False, default="Update bio")
    lastname = models.CharField(max_length=100, unique=False, default="Update bio")
    displayimage = models.ImageField(upload_to='', null=True, blank=True, verbose_name="")
    status = models.TextField(max_length=140)
    #email = models.EmailField(max_length=254)
    def save(self,*args,**kwargs):
        super(Bio,self).save(*args,**kwargs)
        #img=Image.open(self.displayimage.path)
        #img.save(self.displayimage.path)

    def __str__(self):
        return self.firstname+" "+self.lastname+": "+str(self.displayimage)
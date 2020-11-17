# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from picklefield.fields import PickledObjectField
# Create your models here.
class OauthCreds(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE, related_name = "data")
	creds = PickledObjectField(null = True,default = None)

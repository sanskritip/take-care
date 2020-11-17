from django.contrib import admin
from .models import Follow,Like,Tag,Saves
# Register your models here.
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Tag)
admin.site.register(Saves)

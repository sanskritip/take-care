from django.contrib import admin
from .models import Bio
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'user')
    list_filter = ("user",)
    search_fields = ['firstname','lastname']
    prepopulated_fields = {'slug': ('firstname',)}

admin.site.register(Bio)
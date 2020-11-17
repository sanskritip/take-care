from django.contrib import admin
from .models import Picture, PComment

# Register your models here.

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on', 'image')
    list_filter = ("status",)
    search_fields = ['titlepic','image']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'picture', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(PComment,CommentAdmin)
admin.site.register(Picture,PictureAdmin)



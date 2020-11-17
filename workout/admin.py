from django.contrib import admin
from .models import Workout, WComment

# Register your models here.

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['titlevid','videofile']
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'workout', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(WComment,CommentAdmin)
admin.site.register(Workout,WorkoutAdmin)


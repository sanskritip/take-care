from . import views
from django.urls import path

urlpatterns = [
    path('addplaylist/',views.add_playlist,name='addplaylist'),
    path('save_library/<playlist_id>',views.save_library,name='save_library'),
]

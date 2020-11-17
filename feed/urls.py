from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('start-page',views.startup, name = 'start-page'),
    path('dashboard/',views.dashboard, name = 'dashboard'),
    path('explore/',views.explore, name = 'explore'),
    path('newsfeed/', views.newsfeed, name = 'newsfeed'),
    path('saved/', views.saved, name = 'saved'),
    path('followSet/<username>',views.followSet,name = 'followSet'),
    path('profile/<username>',views.profile,name = 'profile'),
    path('blogs/',include('blogs.urls')),
    path('workout/',include('workout.urls')),
    path('picture/',include('posts.urls')),
    path('spotify/',include('spotify.urls')),
    path('test/', views.test),
    path('bio_update/',views.bio_update,name='bio_update'),
    path('tags/',views.tagView,name = 'random_tagview'),
    path('fit/',include('fit_data.urls')),
    path('createSpotifyUser/',views.createSpotifyUser,name = "createSpotifyUser")
]

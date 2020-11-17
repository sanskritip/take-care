
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.landing,name='landing'),
    path('login/',views.loginUser, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('trainer_register/', views.trainer_register, name = 'trainer-register'),
    path('trainee_register/',views.trainee_register,name = 'trainee-register'),
    path('logout/',views.logoutUser,name = 'logout'),

    path('',include('feed.urls')),
    #testing paths
    #path('trainer/', views.trainer, name = 'trainer-feed'),
    #path('trainee/', views.trainee, name = 'trainee-feed'),
]

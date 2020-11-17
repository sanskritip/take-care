from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.start,name = 'auth_display'),
    path('oauth/',views.oauthCallback,name = 'auth_callback'),
    path('glogout/',views.logout_google,name = 'googlelogout'),
    path('extra/',views.extra,name="extra")
]

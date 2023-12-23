from django.contrib import admin
from django.urls import path, include
from Connect_Web import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]


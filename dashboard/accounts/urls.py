from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
   	
    # Generic
   	path('dashboard/', views.dashboard, name='dashboard'),

   	# Auth URLs
   	path('signup/', views.signupuser, name='signupuser'),
   	path('login/', views.loginuser, name='loginuser'),
   	path('logout/', views.logoutuser, name='logoutuser'),


]

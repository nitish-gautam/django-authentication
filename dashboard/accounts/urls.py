from django.urls import path, include
from . import views

urlpatterns = [
    # Generic
    path('', views.home, name="home"),

   	# Auth URLs
   	path('signup/', views.signupuser, name='signupuser'),
   	path('login/', views.loginuser, name='loginuser'),
   	path('logout/', views.logoutuser, name='logoutuser'),
   	
   	## On Sucessfull Login pages URLs
   	path('dashboard/', views.dashboard, name='dashboard'),
   	path('current/', views.current, name='current'),


]

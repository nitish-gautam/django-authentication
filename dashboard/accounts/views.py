from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'accounts/home.html')


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def signupuser(request):
    # if the user request page then showcase the user sign up form
    if request.method == 'GET':
        return render(request, 'accounts/signupuser.html', {'form': UserCreationForm()})

    # Get the form values
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

    # Check if the password matches
    if password == password2:
        # if the user password matches then sign up the user else showcase error and
        # point the user to sign up page with user creation form
        try:
            user = User.objects.create_user(username, password=password)
            user.save()
            login(request, user)
            return redirect('dashboard')
        except IntegrityError:
            return render(request, 'accounts/signupuser.html', {'form': UserCreationForm(), 'error': 'Username is not available try other username'})
    else:
        return render(request, 'accounts/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def loginuser(request):
    # Django provide AuthenticationForm to for login specific fearures
    if request.method == 'GET':
        return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm()})
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            # To authenticate username and password should match
            user = authenticate(request, username=username, password=password)

            if user is None:
                return render(request, 'accounts/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match'})
            else:
                login(request, user)
                return redirect('dashboard')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def current(request):
    return render(request, 'accounts/current.html')

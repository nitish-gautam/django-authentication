from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def dashboard(request):
    context = {}
    return render(request, 'accounts/dashboard.html', context)

def signupuser(request):
    context = {}
    return render(request, 'accounts/signupuser.html', context)

def loginuser(request):
    context = {}
    return render(request, 'accounts/loginuser.html', context)

def logoutuser(request):
    context = {}
    return render(request, 'accounts/home.html', context)

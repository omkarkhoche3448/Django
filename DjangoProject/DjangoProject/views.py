from django.http import HttpResponse
from django.shortcuts import render
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'website/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def home(request):
    return render(request, 'website/home.html',{'user': request.user})

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')



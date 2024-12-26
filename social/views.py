from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as m
from .forms import ProfileCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Home
def home(request):
    return render(request, 'home.html', {})

# Profile
def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, pk=request.user.pk)
        return redirect('view-profile', slug=profile.slug)
    else:
        m.success(request, 'You are not logged in.')
        return redirect('login')

# View profile
def view_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    return render(request, 'profile.html', {'p': profile})

# Register
def register(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            m.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            m.error(request, 'Please correct the errors below.')
    else:
        form = ProfileCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            m.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            m.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'login.html', {})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        m.success(request, 'You have been logged out successfully.')
        return redirect('login')
    else:
        m.warning(request, 'You are not logged in.')
        return redirect('login')

def delete_account(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile, pk=request.user.pk)
        if request.method == 'POST':
            user.delete()
            m.success(request, 'Your profile has been deleted successfully.')
            return redirect('home')
        return render(request, 'delete-account.html', {})
    else:
        m.warning(request, 'You need to be logged in to delete your profile.')
        return redirect('login')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages as msg
from django.contrib.auth import login, logout, authenticate

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            msg.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form.as_div()})

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            msg.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            msg.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'accounts/login.html', {})

# Logout
def logout_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            logout(request)
            msg.info(request, 'You have been logged out successfully.')
            return redirect('home')
        return render(request, 'accounts/logout.html', {})
    else:
        msg.warning(request, 'You are not logged in.')
        return redirect('login')
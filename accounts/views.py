from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import CustomUser
from .forms import RegisterForm, UpdateUserForm

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'accounts/login.html', {})

# Logout
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
    else:
        messages.warning(request, 'You are not logged in.')
    return redirect('login')

# Profile
def profile(request):
    user = get_object_or_404(CustomUser, pk=request.user.pk)
    return render(request, 'accounts/profile.html', {'u': user})

# Update
def update(request):
    if request.user.is_authenticated:
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated successfully.')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors below.')
        else:
            form = UpdateUserForm(instance=user)
        return render(request, 'accounts/update.html', {'form': form})
    else:
        messages.error(request, 'You need to log in to update your profile.')
        return redirect('login')

# Delete Account
def delete(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            request.user.delete()
            messages.success(request, 'Your account has been deleted successfully.')
            return redirect('register')
        return render(request, 'accounts/delete.html', {})
    else:
        messages.error(request, 'You need to log in to delete your account.')
        return redirect('login')

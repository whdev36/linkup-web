from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AccountForm, AccountChangeForm
from django.contrib.auth import login, logout, authenticate
from .models import Account
from django.contrib import messages

# Register user
def register_account(req):
	if req.method == 'POST':
		form = AccountForm(req.POST)
		if form.is_valid():
			form.save()
			messages.success(req, 'Registration successful! You can now log in.')
			return redirect('login')
		else:
			messages.warning(req, 'Please correct the errors below.')
	else:
		form = AccountForm()
	return render(req, 'account/register.html', {'form': form})

# Login user
def login_account(req):
	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(req, username=username, password=password)
		if user is not None:
			login(req, user)
			messages.success(req, 'Login successful! Welcome back.')
			return redirect('account')
		else:
			messages.error(req, 'Invalid username or password. Please try again.')
	return render(req, 'account/login.html', {})

# Logout user
def logout_account(req):
	if req.user.is_authenticated:
		logout(req)
		messages.info(req, 'You have been logged out successfully.')
		return redirect('login')
	else:
		messages.warning(req, 'You are not logged in.')
		return redirect('home')

# Update user
def update_account(req):
	if req.user.is_authenticated:
		user = get_object_or_404(Account, pk=req.user.pk)
		if req.method == 'POST':
			form = AccountChangeForm(req.POST, req.FILES, instance=user)
			if form.is_valid():
				form.save()
				messages.success(req, 'Your profile has been updated successfully.')
				return redirect('account')
		else:
			form = AccountChangeForm(instance=user)
		return render(req, 'account/update.html', {'form': form})
	else:
		messages.warning(req, 'You need to be logged in to update your profile.')
		return redirect('login')

# Delete user
def delete_account(req):
	return HttpResponse('delete')

# Account
def account(req):
	return HttpResponse('account')
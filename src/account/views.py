from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AccountForm, AccountChangeForm
from django.contrib.auth import login, logout, authenticate
from .models import Account

# Register user
def register_account(req):
	if req.method == 'POST':
		form = AccountForm(req.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
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
			return redirect('account')
	return render(req, 'account/login.html', {})

# Logout user
def logout_account(req):
	logout(req)
	return redirect('register')

# Update user
def update_account(req):
	if req.user.is_authenticated:
		user = get_object_or_404(Account, pk=req.user.pk)
		if req.method == 'POST':
			form = AccountChangeForm(req.POST, req.FILES, instance=user)
			if form.is_valid():
				form.save()
				return HttpResponse('Your profile has been updated successfully.')
		else:
			form = AccountChangeForm(instance=user)
		return render(req, 'account/update.html', {'form': form})
	else:
		return HttpResponse('You need to be logged in to update your profile.')

# Delete user
def delete_account(req):
	return HttpResponse('delete')

# Account
def account(req):
	return HttpResponse('account')
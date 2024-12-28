from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AccountForm

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
	return HttpResponse('login')

# Logout user
def logout_account(req):
	return HttpResponse('logout')

# Update user
def update_account(req):
	return HttpResponse('update')

# Delete user
def delete_account(req):
	return HttpResponse('delete')


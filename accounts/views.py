from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages as msg

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            msg.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            msg.success(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form.as_div()})

# Login
def login_user(request):
    return HttpResponse('login')

# Logout
def logout_user(request):
    return HttpResponse('logout')

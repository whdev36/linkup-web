from django.shortcuts import render

# Home
def home(request):
    return render(request, 'home.html', {})

# Profile
def profile(request):
    return render(request, 'profile.html', {})

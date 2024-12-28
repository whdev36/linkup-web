from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as m
from .forms import ProfileCreationForm, ProfileChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Post
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Home
def home(request):
    posts = Post.objects.select_related('author').all()
    return render(request, 'home.html', {'posts': posts})

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
    followers_count = profile.followers.count()
    following_count = profile.follows.count()
    return render(request, 'profile.html', {'p': profile, 'followers_count': followers_count,
        'following_count': following_count,})

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

def update_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Profile, pk=request.user.pk)
        print(user)
        if request.method == 'POST':
            form = ProfileChangeForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                m.success(request, 'Your profile has been updated successfully.')
                return redirect('view-profile', slug=user.slug)
        else:
            form = ProfileChangeForm(instance=user)
        return render(request, 'update-profile.html', {'form': form})
    else:
        m.warning(request, 'You need to be logged in to update your profile.')
        return redirect('home')

def read_users(request):
    users = Profile.objects.all()
    return render(request, 'read-users.html', {'users': users})

def read_user(request, slug):
    user = get_object_or_404(Profile, slug=slug)
    followers_count = user.followers.count()
    following_count = user.follows.count()
    return render(request, 'read-user.html', {'p': user, 'followers_count': followers_count,
        'following_count': following_count,})

@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(Profile, id=user_id)
    request.user.follows.add(user_to_follow)
    return redirect('read-user', slug=user_to_follow.username)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(Profile, id=user_id)
    request.user.follows.remove(user_to_unfollow)
    return redirect('read-user', slug=user_to_unfollow.username)

# Profile
@login_required
def profile(request):
    profile = get_object_or_404(Profile, pk=request.user.pk)
    return redirect('view-profile', slug=profile.slug)

# View profile
@login_required
def view_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    followers_count = profile.followers.count()
    following_count = profile.follows.count()
    return render(request, 'profile.html', {
        'p': profile,
        'followers_count': followers_count,
        'following_count': following_count,
    })

# Post List
def post_list(request):
    posts = Post.objects.select_related('author').all()
    return render(request, 'post_list.html', {'posts': posts})

# Post Create
@login_required
def post_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)
            m.success(request, 'Post created successfully.')
            return redirect('post_list')
        else:
            m.error(request, 'Content cannot be empty.')
    return render(request, 'post_form.html', {})

# Post Update
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.content = request.POST.get('content', post.content)
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        m.success(request, 'Post updated successfully.')
        return redirect('post_list')
    return render(request, 'post_form.html', {'post': post})

# Post Delete
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        m.success(request, 'Post deleted successfully.')
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})

# Like / Unlike Post
@login_required
def post_like_toggle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({"liked": liked, "like_count": post.likes.count()})
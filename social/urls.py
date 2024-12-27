from django.urls import path
from . import views

# Using: create, update, read, delete
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('profile/<slug:slug>/', views.view_profile, name='view-profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('read-users/', views.read_users, name='read-users'),
    path('read-user/<slug:slug>/', views.read_user, name='read-user'),
    path('follow/<int:user_id>/', views.follow_user, name='follow'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow'),
]
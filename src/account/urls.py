# account/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register_account, name='register'),
	path('login/', views.login_account, name='login'),
	path('logout/', views.logout_account, name='logout'),
	path('update/', views.update_account, name='update-account'),
	path('delete/', views.delete_account, name='delete-account'),
	path('', views.my_account, name='account'),
	path('users/', views.users, name='users'),
	path('follow/<slug:slug>/', views.follow_user, name='follow'),
	path('unfollow/<slug:slug>/', views.unfollow_user, name='unfollow'),
	path('<slug:slug>/', views.view_account, name='view-account'),
]
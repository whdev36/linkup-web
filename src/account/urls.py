# account/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register_account, name='register'),
	path('login/', views.login_account, name='login'),
	path('logout/', views.logout_account, name='logout'),
	path('update/', views.update_account, name='update-profile'),
	path('delete/', views.delete_account, name='delete-account'),
	path('', views.account, name='account'),
]
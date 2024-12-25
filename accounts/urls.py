from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='account'),
    path('update/', views.update, name='update-account'),
    path('delete/', views.delete, name='delete-account'),
]
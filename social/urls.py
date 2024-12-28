from django.urls import path
from . import views
# from .views import (
#     PostListView,
#     PostCreateView,
#     PostUpdateView,
#     PostDeleteView,
#     PostLikeToggleView,
# )

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

    path('posts/', views.post_list, name='post_list'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/update/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:pk>/like/', views.post_like_toggle, name='post_like_toggle'),

    # path('posts/', PostListView.as_view(), name="post_list"),
    # path('post/new/', PostCreateView.as_view(), name="post_create"),
    # path('post/<int:pk>/edit/', PostUpdateView.as_view(), name="post_update"),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    # path('post/<int:pk>/like/', PostLikeToggleView.as_view(), name="post_like_toggle"),
]
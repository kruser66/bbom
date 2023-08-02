from django.urls import path
from django.contrib.auth.decorators import login_required

from blog import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path(
        'add/',
        login_required(
            views.PostView.as_view(),
            login_url='login'
        ),
        name='add_post'
    ),
    path('delete/<id>', views.delete_post, name='delete_post'),
    path('users/<id>/posts', views.posts, name='user_posts'),
    
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
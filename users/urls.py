"""learning_logs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('articles/', views.articles, name='articles'),
    path('articles/<article_id>/', views.article, name='article'),
    path('friends', views.friends, name='friends'),
    path('add_friend/<friend_id>/', views.add_friend, name='add_friend'),
    path('friend_added', views.friend_added, name='friend_added'),
    path('delete_friend/<friend_id>/', views.delete_friend, name='delete_friend'),
    path('friend_deleted', views.friend_deleted, name='friend_deleted'),

]

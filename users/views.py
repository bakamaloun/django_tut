from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .models import Article, Friend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

# custom logout, not used
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticaded_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticaded_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)

def articles(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'users/articles.html', context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    authors = article
    context = {'article': article, 'authors': authors}
    return render(request, 'users/article.html', context)

@login_required
def friends(request):
    users = User.objects.all()
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.users.all()
    context = {'friends': friends, 'users': users}
    return render(request, 'users/friends.html', context)

@login_required
def add_friend(request, friend_id):
    new_friend = User.objects.get(pk=friend_id)
    Friend.add_friend(request.user, new_friend)
    return render(request, 'users/friend_added.html')

def friend_added(request):
    return render(request, 'users/friend_added.html')

@login_required
def delete_friend(request, friend_id):
    old_friend = User.objects.get(pk=friend_id)
    Friend.delete_friend(request.user, old_friend)
    return render(request, 'users/friend_deleted.html')

def friend_deleted(request):
    return render(request, 'users/friend_deleted.html')
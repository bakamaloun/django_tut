from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Many to many examples

class Article(models.Model):
    title = models.CharField(max_length=10)
    authors = models.ManyToManyField('Author', through='Written_by')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=10)
    articles = models.ManyToManyField('Article', through='Written_by')

    def __str__(self):
        return self.name

class Written_by(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Written by'

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.DO_NOTHING)

    @classmethod
    def add_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def delete_friend(cls, current_user, old_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(old_friend)
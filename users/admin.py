from django.contrib import admin

# Register your models here.

from users.models import Author, Article, Written_by, Friend

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Written_by)
admin.site.register(Friend)
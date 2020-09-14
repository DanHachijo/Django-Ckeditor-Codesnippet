from django.contrib import admin
from .models import Category, Difficulty, Post

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Post)
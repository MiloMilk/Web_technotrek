from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = 'name', 'author'
    search_fields = 'name', 'author'
    pass

@admin.register(Comment)
class PageAdmin(admin.ModelAdmin):
    list_display = 'article_id', 'author', 'content'
    pass

@admin.register(Like)
class PageAdmin(admin.ModelAdmin):
    list_display = 'author', 'comment'

from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = 'name', 'author'
    search_fields = 'name', 'author'
    pass
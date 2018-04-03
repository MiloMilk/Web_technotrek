from django.db import models
from django.conf import settings
from categories.models import Category
# Create your models here.


class Post(models.Model):


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="posts", verbose_name=u"Автор")
    name = models.CharField(max_length=255, verbose_name=u"Заголовок")
    categories = models.ManyToManyField(Category, blank=True, related_name="posts", verbose_name=u"Категории")
    bodytext = models.TextField(blank=True, verbose_name=u"Текст")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Пост"
        verbose_name_plural = u"Все посты"
        pass

    def __str__(self):
        return self.name
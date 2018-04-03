from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="category", verbose_name=u"Автор")
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"
        pass

    def __str__(self):
        return self.name
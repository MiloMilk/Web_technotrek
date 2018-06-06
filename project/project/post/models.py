from django.db import models
from django.conf import settings
from categories.models import Category
# Create your models here.


class Post(models.Model):


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="posts", verbose_name=u"Автор")
    name = models.CharField(max_length=255, verbose_name=u"Заголовок")
    categories = models.ManyToManyField(Category, blank=True, related_name="posts", verbose_name=u"Категории")
    bodytext = models.TextField(blank=True, verbose_name=u"Текст")
    image = models.ImageField(blank=True, upload_to='post_image')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Пост"
        verbose_name_plural = u"Все посты"
        pass

    def __str__(self):
        return self.name


class Comment(models.Model):

    class Meta:
        verbose_name = u"Комментарий"
        verbose_name_plural = u"Комментарии"
        db_table = "comments"


    article_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="comments",
                               verbose_name=u"Автор")
#    likes = models.IntegerField(default=0)

    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=u"Комментарий")

    def __str__(self):
        return self.content[0:200]

class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name="likes",
                               verbose_name=u"Автор")

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="commentLike")


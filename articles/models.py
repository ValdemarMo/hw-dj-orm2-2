from django.db import models
from django.db.models import F


class Topic(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='Название')

    class Meta:
        ordering = ['name']
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    fields = models.ManyToManyField(Topic, through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='scopes', verbose_name='Разделы')
    is_main = models.BooleanField()

    class Meta:
        ordering = ['-is_main', F('topic').name]
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
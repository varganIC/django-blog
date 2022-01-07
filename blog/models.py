from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, default='', unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Message(models.Model):
    article = models.CharField("Тема письма", max_length=100, default='', unique=True)
    email = models.EmailField("Почта пользователя", unique=True)
    text = models.TextField("Текст сообщения")

    def __str__(self):
        return f'Письмо: {self.article}'

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class Comment(models.Model):
    text = models.TextField("Сообщение*")
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    title = models.ForeignKey(News, verbose_name='Статья', on_delete=models.CASCADE)
    date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
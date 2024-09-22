from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    anons = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

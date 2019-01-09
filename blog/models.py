from django.db import models
from django.utils import timezone


class Medicine(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Название = models.CharField(max_length=200)
    Форма_выпуска = models.TextField()
    Способ_применения = models.TextField()
    Противопоказания = models.CharField(max_length=500)
    Выдача = models.CharField(max_length=100)
    Срок_годности = models.CharField(max_length=30)
    Наличие = models.CharField(max_length=30)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Название

class Request(models.Model): #заявка
    Название = models.CharField(max_length=200)
    Форма_выпуска = models.CharField(max_length=200)
    Дозировка = models.CharField(max_length=200)
    Ваш_email_или_номер_телефона = models.CharField(max_length=200)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Название



# Create your models here.

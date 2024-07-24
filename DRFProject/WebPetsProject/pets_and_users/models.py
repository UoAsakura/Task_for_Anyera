from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pet(models.Model):
    """
    Модель нашего петомца
    """
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.FileField(upload_to='photos', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return self.name
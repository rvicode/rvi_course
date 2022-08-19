from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=60, verbose_name='ایمیل')
    Description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    image = models.ImageField(null=True, blank=True, verbose_name='تصویر')

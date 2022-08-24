from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    profile_pic = models.ImageField(null=True, blank=True, verbose_name='تصویر')
    is_teacher = models.BooleanField(default=False, verbose_name='معلم است')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'اکانت کاربر'
        verbose_name_plural = 'اکانت های کاربر'
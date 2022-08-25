from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره همراه')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    profile_pic = models.ImageField(null=True, blank=True, verbose_name='تصویر', upload_to='image_profiles/')
    is_teacher = models.BooleanField(default=False, verbose_name='معلم است')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'اکانت کاربر'
        verbose_name_plural = 'اکانت های کاربر'

    def __str__(self):
        return self.email

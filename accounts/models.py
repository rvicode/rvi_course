from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=200, verbose_name='ایمیل')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره همراه')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    profile_pic = models.ImageField(null=True, blank=True, verbose_name='تصویر', upload_to='image_profiles/')
    is_teacher = models.BooleanField(default=False, verbose_name='معلم است')
    is_team_member = models.BooleanField(default=False, verbose_name='عضو تیم است')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    instagram = models.CharField(max_length=200, verbose_name='اینستاگرام', null=True, blank=True)
    whatsapp = models.CharField(max_length=200, verbose_name='واتساپ', null=True, blank=True)
    telegram = models.CharField(max_length=200, verbose_name='تلگرام', null=True, blank=True)
    facebook = models.CharField(max_length=200, verbose_name='فیسبوک', null=True, blank=True)
    twitter = models.CharField(max_length=200, verbose_name='تویتر', null=True, blank=True)
    reddit = models.CharField(max_length=200, verbose_name='ردیت', null=True, blank=True)
    github = models.CharField(max_length=200, verbose_name='گیت هاب', null=True, blank=True)
    linkedin = models.CharField(max_length=200, verbose_name='فیسبوک', null=True, blank=True)

    class Meta:
        verbose_name = 'اکانت کاربر'
        verbose_name_plural = 'اکانت های کاربر'

    def __str__(self):
        return self.username

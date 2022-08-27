from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name='دسته بندی')
    title = models.CharField(max_length=60, verbose_name='مقدمه')
    description = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='media/Courses/image', verbose_name='تصویر')
    file = models.FileField(upload_to='media/Courses', verbose_name='فایل')
    time_video = models.CharField(max_length=20, verbose_name='زمان ویدیو')
    created = models.DateField(auto_now_add=True, verbose_name='تاریخ نشر')
    update = models.DateField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment', verbose_name='کاربر')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comment', verbose_name='دوره')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replay',
                               verbose_name='پاسخ به نظر')
    body = models.TextField(verbose_name='نظر')
    created = models.DateField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return f'{self.body}'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

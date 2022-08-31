from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


class Field(models.Model):
    title = models.CharField(max_length=100, verbose_name='فریمورک')

    class Meta:
        verbose_name = 'فریمورک'
        verbose_name_plural = 'فریمورک ها'

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=100, verbose_name='زبان برنامه نویسی')

    class Meta:
        verbose_name = 'زیان برنامه نویسی'
        verbose_name_plural = 'زبان های برنامه نویسی'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=60, verbose_name='حوزه برنامه نویسی')

    class Meta:
        verbose_name = 'حوزه برنامه نویسی'
        verbose_name_plural = 'حوزه های برنامه نویسی'

    def __str__(self):
        return self.title


class Course(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=60, verbose_name='مقدمه')
    category = models.ManyToManyField(Category, related_name='category',
                                      verbose_name='حوزه برنامه نویسی', null=True, blank=True)
    field = models.ManyToManyField(Field, related_name='field', verbose_name='فریمورک', null=True, blank=True)
    language = models.ManyToManyField(Language, related_name='language',
                                      verbose_name='زبان برنامه نویسی', null=True, blank=True)
    description = models.TextField(verbose_name='متن', null=True, blank=True)
    image = models.ImageField(upload_to='media/Courses/image', verbose_name='تصویر', null=True, blank=True)
    file = models.FileField(upload_to='media/Courses/video', verbose_name='فایل', null=True, blank=True)
    time_video = models.CharField(max_length=20, verbose_name='زمان ویدیو')
    created = models.DateField(auto_now_add=True, verbose_name='تاریخ نشر')
    update = models.DateField(auto_now=True, verbose_name='تاریخ بروز رسانی')
    slug = models.SlugField()

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:detail_video', args=[self.id])


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


class AboutUs(models.Model):
    title = models.CharField(max_length=50, verbose_name='موضوع')
    description = models.TextField(verbose_name='توضیحات')
    our_products = models.TextField(verbose_name='محصولات ما')

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'

    def __str__(self):
        return self.title

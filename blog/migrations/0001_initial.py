# Generated by Django 4.1 on 2022-08-24 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='مقدمه')),
                ('description', models.TextField(verbose_name='بدنه')),
                ('image', models.ImageField(upload_to='media/Courses/image')),
                ('file', models.FileField(upload_to='media/Courses', verbose_name='فایل')),
                ('time_video', models.CharField(max_length=20, verbose_name='زمان ویدیو')),
                ('created', models.DateField(auto_now_add=True, verbose_name='تاریخ نشر')),
                ('update', models.DateField(auto_now=True, verbose_name='تاریخ بروز رسانی')),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='نویسنده')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='نظر')),
                ('created', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.course', verbose_name='دوره')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replay', to='blog.comment', verbose_name='پاسخ به نظر')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='accounts.customuser', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]

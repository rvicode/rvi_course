# Generated by Django 4.1 on 2022-08-15 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'دوره', 'verbose_name_plural': 'دوره ها'},
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to='media/Courses/image'),
            preserve_default=False,
        ),
    ]

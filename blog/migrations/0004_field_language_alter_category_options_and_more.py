# Generated by Django 4.1 on 2022-08-28 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_course_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='فریمورک')),
            ],
            options={
                'verbose_name': 'فریمورک',
                'verbose_name_plural': 'فریمورک ها',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='زبان برنامه نویسی')),
            ],
            options={
                'verbose_name': 'زیان برنامه نویسی',
                'verbose_name_plural': 'زبان های برنامه نویسی',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'حوزه برنامه نویسی', 'verbose_name_plural': 'حوزه های برنامه نویسی'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=60, verbose_name='حوزه برنامه نویسی'),
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='field',
            field=models.ManyToManyField(related_name='field', to='blog.field', verbose_name='فریمورک'),
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ManyToManyField(related_name='language', to='blog.language', verbose_name='زبان برنامه نویسی'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ManyToManyField(related_name='category', to='blog.category', verbose_name='حوزه برنامه نویسی'),
        ),
    ]

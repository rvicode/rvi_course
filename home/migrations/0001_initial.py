# Generated by Django 4.1 on 2022-08-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='موضوع')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('our_products', models.TextField(verbose_name='محصولات ما')),
            ],
        ),
    ]

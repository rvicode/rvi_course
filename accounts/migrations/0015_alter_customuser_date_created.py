# Generated by Django 4.1 on 2022-08-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_customuser_is_team_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت'),
        ),
    ]

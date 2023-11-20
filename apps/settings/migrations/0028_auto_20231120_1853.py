# Generated by Django 3.2.20 on 2023-11-20 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0027_auto_20231120_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='Аддресс'),
        ),
        migrations.AddField(
            model_name='settings',
            name='email',
            field=models.EmailField(default='', max_length=100, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='settings',
            name='phone',
            field=models.CharField(default='', max_length=100, verbose_name='Телефон'),
        ),
    ]

# Generated by Django 3.2.20 on 2023-11-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_auto_20231120_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservetion',
            name='date_guest',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservetion',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservetion',
            name='pers_guest',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='reservetion',
            name='time_guest',
            field=models.CharField(default='', max_length=100),
        ),
    ]
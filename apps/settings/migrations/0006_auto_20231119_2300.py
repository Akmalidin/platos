# Generated by Django 3.2.20 on 2023-11-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20231119_2240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='days',
            options={'verbose_name': 'Рабочее время', 'verbose_name_plural': 'Наши рабочие времена'},
        ),
        migrations.AlterField(
            model_name='days',
            name='time',
            field=models.CharField(help_text='Пример: 8 AM - 8 PM', max_length=255, verbose_name='Время'),
        ),
    ]

# Generated by Django 3.2.20 on 2023-11-20 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0020_auto_20231120_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commands',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='commands',
            name='google',
        ),
        migrations.RemoveField(
            model_name='commands',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='commands',
            name='twitter',
        ),
    ]

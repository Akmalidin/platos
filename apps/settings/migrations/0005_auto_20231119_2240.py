# Generated by Django 3.2.20 on 2023-11-19 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_auto_20231119_2228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(help_text='Пример: Понидельник-Пятница', max_length=255, verbose_name='Радочие дни')),
                ('time', models.DateTimeField(verbose_name='Время')),
            ],
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name': 'Наш ресторан', 'verbose_name_plural': 'Наш ресторан'},
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='days',
        ),
    ]
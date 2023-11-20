from django.db import models
from datetime import datetime
class Settings(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название сайта'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    address = models.CharField(
        max_length=255,
        verbose_name = 'Аддресс', default=''
    )
    phone = models.CharField(
        max_length=100,
        verbose_name='Телефон', default=''
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Электронная почта', default=''
    )
    def __str__(self):
        return f'{self.title} - {self.description}'
    class Meta:
        verbose_name = 'Основные настройки'
        verbose_name_plural = 'Основные настройки'

class Slider(models.Model):
    image = models.ImageField(
        upload_to='slider/',
        verbose_name='Изображение слайдера'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок слайда'
    )
    description = models.TextField(
        verbose_name='Описание слайдера'
    )
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

class History(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='history/',
        verbose_name='Изображение'
    )
    sec_image = models.ImageField(
        upload_to='history/',
        verbose_name='Заднее фото'
    )
    suptitle = models.CharField(
        max_length=100,
        verbose_name='Подзаголовок'
    )
    second_desc = models.TextField(
        verbose_name='Второе описание'
    )
    propic = models.ImageField(
        upload_to='history_propic/',
        verbose_name='Фото Подпись'
    )
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'

class Restaurant(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = 'Заголовок'
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name='Подзагаловок'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='restaurant/',
        verbose_name='Изображение'
    )
    sec_image = models.ImageField(
        upload_to='restaurant/',
        verbose_name='Заднее фото'
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    
    class Meta:
        verbose_name = 'Наш ресторан'
        verbose_name_plural = 'Наш ресторан'
class Days(models.Model):
    days = models.CharField(
        max_length=255,
        verbose_name='Радочие дни',
        help_text='Пример: Понидельник-Пятница'
    )
    time = models.CharField(
        max_length=255,
        verbose_name='Время',
        help_text='Пример: 8 AM - 8 PM'
    )
    def __str__(self):
        return f'{self.days} - {self.time}'
    
    class Meta:
        verbose_name = 'Рабочее время'
        verbose_name_plural = 'Наши рабочие времена'

class Special(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Загаловок'
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name='Подзагаловок'
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name = 'Загаловок Специальных блюд'
        verbose_name_plural = 'Загаловок Специальных блюд'

class Special_foods(models.Model):
    
    image = models.ImageField(
        upload_to='special_media/',
        verbose_name='Фото'
    )
    block_title = models.CharField(
        max_length=100,
        verbose_name='Загаловок Фотографии'
    )
    block_suptitle = models.CharField(
        max_length=100,
        verbose_name='Подзагаловок Фотографии'
    )
    block_price = models.CharField(
        max_length=100,
        verbose_name='Цена'
    )
    block_time = models.CharField(
        max_length=100,
        verbose_name='Тип блюдо',
        help_text='Завтрак, Обед, Ужин, Десерт'
    )
    def __str__(self):
        return f'{self.block_title} - {self.block_suptitle}'
    class Meta:
        verbose_name = 'Специальные блюды'
        verbose_name_plural = 'Специальные блюды'
class Menu(models.Model):
    title = models.CharField (
    max_length=100,
    verbose_name='Загаловок'
    )
    suptitle = models.CharField (
    max_length=255,
    verbose_name='Подзагаловок'
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
class Lunch(models.Model):
    title = models.CharField (
    max_length=100,
    verbose_name='Загаловок'
    )
    suptitle = models.CharField (
    max_length=100,
    verbose_name='Описание'
    )
    price = models.CharField (
    max_length=100,
    verbose_name='Цена'
    )
    img = models.ImageField (
        upload_to='Menu/',
        verbose_name='Фото'
    )
    new = models.BooleanField (
        verbose_name='Новое',
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name='Ланч'
        verbose_name_plural ='Ланч'

class Dinner(models.Model):
    title = models.CharField (
    max_length=100,
    verbose_name='Загаловок'
    )
    suptitle = models.CharField (
    max_length=100,
    verbose_name='Описание'
    )
    price = models.CharField (
    max_length=100,
    verbose_name='Цена'
    )
    img = models.ImageField (
        upload_to='Menu/',
        verbose_name='Фото'
    )
    new = models.BooleanField (
        verbose_name='Новое',
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name='Ужин'
        verbose_name_plural ='Ужин'
    
class Dessert(models.Model):
    title = models.CharField (
    max_length=100,
    verbose_name='Загаловок'
    )
    suptitle = models.CharField (
    max_length=100,
    verbose_name='Описание'
    )
    price = models.CharField (
    max_length=100,
    verbose_name='Цена'
    )
    img = models.ImageField (
        upload_to='Menu/',
        verbose_name='Фото'
    )
    new = models.BooleanField (
        verbose_name='Новое',
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name='Десерт'
        verbose_name_plural ='Десерт'

class Drinks(models.Model):
    title = models.CharField (
    max_length=100,
    verbose_name='Загаловок'
    )
    suptitle = models.CharField (
    max_length=100,
    verbose_name='Описание'
    )
    price = models.CharField (
    max_length=100,
    verbose_name='Цена'
    )
    img = models.ImageField (
        upload_to='Menu/',
        verbose_name='Фото'
    )
    new = models.BooleanField (
        verbose_name='Новое',
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name='Напитки'
        verbose_name_plural ='Напитки'




class Command(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок', default=''
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name = 'Подзагаловок', default=''
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name = 'Название команды'
        verbose_name_plural = 'Название команды'

class Commands(models.Model):
    img = models.ImageField(
        upload_to='commands/',
        verbose_name='Фото повара'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя повара'
    )
    special = models.CharField(
        max_length=100,
        verbose_name='Специальность'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    facebook = models.URLField(
        blank=True,
        verbose_name='Facebook ссылка'
    )
    twitter = models.URLField(
        blank=True,
        verbose_name='Twitter ссылка'
    )
    google = models.URLField(
        blank=True,
        verbose_name='google ссылка'
    )
    instagram = models.URLField(
        blank=True,
        verbose_name='instagram ссылка'
    )
    def __str__(self):
        return f'{self.name} - {self.special}'
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
    
class Reservetion(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name = 'Заголовок', default=''
    )
    suptitle = models.CharField(
        max_length=100,
        verbose_name = 'Заголовок', default=''
    )
    def __str__(self):
        return f'{self.title} - {self.suptitle}'
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

class Opit(models.Model):
    number = models.CharField(
        max_length=255,
        verbose_name='Число опыта'
    )
    title = models.CharField(
        max_length=255,
        verbose_name = 'Заголовок'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return f'{self.title} - {self.desc}'
    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыты'

class Blog(models.Model):
    img = models.ImageField(
        upload_to='blog/',
        verbose_name='Фото'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    data = models.CharField(
        max_length=255,
        verbose_name='Дата',
        help_text='December 16, 2015 /  Food /  3 comments'
    )
    desc = models.TextField(
        verbose_name='Описание'
    )
    facebook = models.URLField(
        blank=True,
        verbose_name='Facebook ссылка'
    )
    twitter = models.URLField(
        blank=True,
        verbose_name='Twitter ссылка'
    )
    google = models.URLField(
        blank=True,
        verbose_name='google ссылка'
    )
    instagram = models.URLField(
        blank=True,
        verbose_name='instagram ссылка'
    )
    def __str__(self):
        return f'{self.title} - {self.desc}'
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


def lector_directory_path(instance, filename):
    return f'lector_{instance.username}/{filename}'


class Lector(models.Model):
    username = models.SlugField(max_length=255, primary_key=True, unique=True, db_index=True, verbose_name='URL')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Отчество')
    description = models.TextField(null=True, blank=True, verbose_name='О лекторе', help_text='Будут отображаться '
                                                                                              'в карточке лектора.')
    achievements = RichTextField(null=True, blank=True, verbose_name='Достижения', help_text='Будут отображаться '
                                                                                                'на странице лектора.'
                                                                                                ' Чтобы сделать пункт '
                                                                                                '- перед предложением '
                                                                                                'необходимо добавить '
                                                                                                '** (две '
                                                                                                'звёздочки).')
    main_photo = models.ImageField(upload_to=lector_directory_path, null=True, blank=True, verbose_name='Фото в списке')
    second_photo = models.ImageField(upload_to=lector_directory_path, null=True, blank=True, verbose_name='Фото внутри')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'
        ordering = ['first_name']


class SeminarSphere(models.Model):
    sphere = models.CharField(max_length=255, verbose_name='Название сферы семинаров', primary_key=True, unique=True)

    def __str__(self):
        return f'{self.sphere}'


class SeminarFormat(models.Model):
    format = models.CharField(max_length=255, verbose_name='Формат', primary_key=True, unique=True)

    def __str__(self):
        return f'{self.format}'

    class Meta:
        verbose_name = 'Формат'
        verbose_name_plural = 'Форматы семинаров'


class Seminar(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True, unique=True, db_index=True, verbose_name='URL')
    title = models.TextField(verbose_name="Заголовок")
    for_whom = models.TextField(verbose_name="Целевая аудитория", null=True, blank=True)
    description = models.TextField(verbose_name='О семинаре', null=True, blank=True)
    regulation = RichTextField(verbose_name='Регламент', help_text='ДОБАВИТЬ ОПИСАНИЕ', null=True, blank=True)
    program = RichTextField(verbose_name='Программа', help_text='ДОБАВИТЬ ОПИСАНИЕ', null=True, blank=True)
    sphere = models.ForeignKey(SeminarSphere, on_delete=models.SET_NULL, null=True, verbose_name='Сфера')
    date_start = models.DateField(verbose_name='Дата начала семинара')
    date_end = models.DateField(verbose_name='Дата окончания семинара')
    time_start = models.TimeField(verbose_name='Время начала семинара')
    time_end = models.TimeField(verbose_name='Время окончания семинара')
    lector = models.ForeignKey(Lector, on_delete=models.SET_NULL, null=True, verbose_name="Лектор")
    seminar_format = models.ForeignKey(SeminarFormat, on_delete=models.SET_NULL, verbose_name='Формат семинара', null=True)
    location_city = models.CharField(max_length=255, verbose_name="Город проведения семинара")
    location_place = models.CharField(max_length=255, verbose_name="Место проведения семинара")
    discount = models.TextField(verbose_name='Скидки', null=True, blank=True, help_text='На первой строке - скидка, на второй - условия', default='10%\nдействует на двух и более участников')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_actual = models.BooleanField(default=False, verbose_name='В списке актуальных')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Семинар'
        verbose_name_plural = 'Семинары'
        ordering = ['date_start', 'time_create']


class SeminarPriceItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Например: Запись семинара')
    seminar = models.ForeignKey(Seminar, on_delete=models.SET_NULL, null=True, verbose_name='Семинар')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    features = models.TextField(verbose_name='Дополнения к прайсу', help_text='ДОБАВИТЬ ОПИСАНИЕ')

    def __str__(self):
        return f'{self.id}. {self.title} - {self.price}р'

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы семинаров'
        ordering = ['-price']


def client_directory_path(instance, filename):
    return f'client_{instance}/{filename}'

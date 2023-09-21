from django.db import models


def lector_directory_path(instance, filename):
    return f'lector_{instance.username}/{filename}'


class Lector(models.Model):
    username = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='URL')
    first_name = models.CharField(max_length=100, verbose_name='Фамилия Имя')
    last_name = models.CharField(max_length=100, verbose_name='Отчество')
    description = models.TextField(null=True, blank=True, verbose_name='О лекторе', help_text='Будут отображаться '
                                                                                              'в карточке лектора.')
    achievements = models.TextField(null=True, blank=True, verbose_name='Достижения', help_text='Будут отображаться '
                                                                                                'на странице лектора.'
                                                                                                ' Чтобы сделать пункт '
                                                                                                '- перед предложением '
                                                                                                'необходимо добавить '
                                                                                                '** (две '
                                                                                                'звёздочки).')
    main_photo = models.ImageField(upload_to=lector_directory_path, null=True, blank=True, verbose_name='Фото',
                                   help_text='Будет отображаться на странице с лекторами')
    second_photo = models.ImageField(upload_to=lector_directory_path, null=True, blank=True, verbose_name='Фото',
                                     help_text='Будет отображаться на странице лектора')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Лектор'
        verbose_name_plural = 'Лекторы'
        ordering = ['first_name']


class SeminarPriceItemFuture(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Дополнение к прайсу'
        verbose_name_plural = 'Дополнения к прайсу'
        ordering = ['title']


class SeminarPriceItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Например: Запись семинара')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    features = models.ManyToManyField(SeminarPriceItemFuture)

    def __str__(self):
        return f'{self.id}. {self.title} - {self.price}р'

    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = 'Прайсы семинаров'
        ordering = ['-price']


class SeminarSphere(models.Model):
    sphere = models.CharField(max_length=255, verbose_name='Название сферы семинаров', primary_key=True, unique=True)

    def __str__(self):
        return f'{self.sphere}'


class SeminarProgram(models.Model):
    program = models.TextField(verbose_name='Программа', help_text='&lt;b&gt;<b>жирный</b>&lt;/b&gt; <b>|</b> '
                                                                   '&lt;i&gt;<i>курсив</i>&lt;/i&gt;')
    program_date = models.DateField(verbose_name='Дата программы')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'{self.program_date} - {self.program}'

    class Meta:
        verbose_name = 'Программа семинара'
        verbose_name_plural = 'Программы семинаров'
        ordering = ['program', 'id']


class SeminarRegulation(models.Model):
    regulation = models.TextField(verbose_name='Регламент', help_text='&lt;b&gt;<b>жирный</b>&lt;/b&gt; <b>|</b> '
                                                                      '&lt;i&gt;<i>курсив</i>&lt;/i&gt;')
    regulation_date = models.DateField(verbose_name='Дата')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Последнее обновление')

    def __str__(self):
        return f'{self.regulation_date} - {self.regulation}'

    class Meta:
        verbose_name = 'Регламент семинара'
        verbose_name_plural = 'Регламент семинаров'
        ordering = ['regulation_date', 'id']


class Seminar(models.Model):
    title = models.TextField(verbose_name="Заголовок")
    description = models.TextField(verbose_name='О семинаре')
    regulation = models.ManyToManyField(SeminarRegulation, verbose_name='Регламент')
    program = models.ManyToManyField(SeminarProgram, verbose_name='Программа')
    sphere = models.ForeignKey(SeminarSphere, on_delete=models.SET_NULL, null=True, verbose_name='Сфера')
    date_start = models.DateTimeField(verbose_name='Начало семинара')
    date_end = models.DateTimeField(verbose_name='Конец семинара')
    lector = models.ForeignKey(Lector, on_delete=models.SET_NULL, null=True, verbose_name="Лектор")
    seminar_format = models.CharField(max_length=255, verbose_name='Форматы семинара')
    location_city = models.CharField(max_length=255, verbose_name="Город проведения семинара")
    location_place = models.CharField(max_length=255, verbose_name="Место проведения семинара")
    price = models.ManyToManyField(SeminarPriceItem, verbose_name='Прайс.')
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
        ordering = ['time_create', 'title']


def client_directory_path(instance, filename):
    return f'client_{instance}/{filename}'

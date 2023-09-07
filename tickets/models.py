from django.db import models

from everest_app.models import Seminar


class EducationTicket(models.Model):
    org_name = models.CharField(max_length=255, verbose_name='Название организации')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f'{self.org_name} number: {self.phone_number}'

    class Meta:
        verbose_name = 'Заявка на корпоративное обучение'
        verbose_name_plural = 'Заявки на корпоративное обучение'
        ordering = ['-id']

class Ticket(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE, verbose_name='Семинар')
    org_name = models.CharField(max_length=255, verbose_name='Название организации')
    ur_address = models.CharField(max_length=255, verbose_name='Юридический адрес')
    mail_address = models.CharField(max_length=255, verbose_name='Почтовый адрес')
    email = models.EmailField(verbose_name='Email', null=True, blank=True)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон')
    job_and_superviser_name = models.CharField(max_length=255, verbose_name='Должность, ФИО руководителя')
    base = models.CharField(max_length=255, verbose_name='Действует на основании')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    kpp = models.CharField(max_length=9, verbose_name='КПП')
    bik = models.CharField(max_length=9, verbose_name='БИК')
    check_acc = models.CharField(max_length=20, verbose_name='Расчетный счет')
    corr_acc = models.CharField(max_length=20, verbose_name='Корр. счёт банка')
    bank_name = models.CharField(max_length=255, verbose_name='Наименование банка')
    contackt_person = models.TextField(verbose_name='Контактное лицо (ФИО, должность, номер телефона)')
    participants = models.TextField(verbose_name='Список участников семинара (ФИО, должность, моб. тел., email.)')
    comment = models.TextField(verbose_name='Комментарий к заявке', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    def __str__(self):
        return f'{self.org_name} inn: {self.inn}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-id']

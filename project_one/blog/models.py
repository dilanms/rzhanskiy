from datetime import timedelta

from django import forms
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


class Company(models.Model):
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    company_name = models.CharField(max_length=254, unique=True)
    company_inn = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return 'Company: {}'.format(self.company_name)


class Affiliater(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    affiliate_name = models.CharField(max_length=254, unique=True)
    affiliate_adres = models.CharField(max_length=254, unique=True)
    tel_number = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return 'Company affiliate: {}'.format(self.affiliate_name)


class Employee(models.Model):
    employee_name = models.CharField(max_length=254, unique=False)
    employee_surname = models.CharField(max_length=254, unique=False)
    employee_patronymic = models.CharField(max_length=254, unique=False)

    def __str__(self):
        return 'Имя работника: {}'.format(self.employee_surname)


class Services(models.Model):
    service_name = models.CharField(max_length=254, unique=False)
    service_price = models.CharField(max_length=254, unique=False)
    service_duration = models.DurationField(default=timedelta())

    def __str__(self):
        return 'Услуга: {}'.format(self.service_name)


class Specialization(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    services_id = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return 'Сотрудник: {}'.format(self.employee_id)
from django.contrib.auth.models import User

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64, null=True)
    location = models.CharField(max_length=64, null=True)
    logo = models.CharField(max_length=128, default="https://place-hold.it/100x60")  # "https://place-hold.it/100x60"
    description = models.CharField(max_length=128, null=True)
    employee_count = models.IntegerField(null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=128, default="https://place-hold.it/100x60")  # "https://place-hold.it/100x60"


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=128, default='Скоро обновим')
    description = models.CharField(max_length=128, default='Добавим позже')
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

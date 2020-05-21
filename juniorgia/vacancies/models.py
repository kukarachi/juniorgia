from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64, null=True)
    location = models.CharField(max_length=64, null=True)
    description = models.TextField(max_length=256, null=True)
    employee_count = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    logo = models.ImageField(upload_to='logos', height_field='height_field', width_field='width_field', null=True)
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='pics', height_field='height_field', width_field='width_field', null=True)
    height_field = models.PositiveIntegerField(default=0)
    width_field = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.TextField(max_length=256, default='Скоро обновим')
    description = models.TextField(max_length=1024, default='Добавим позже')
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return self.title

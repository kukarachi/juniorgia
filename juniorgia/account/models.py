from django.db import models
from django.contrib.auth.models import User

import vacancies.models as vacancy_models


class Application(models.Model):
    written_username = models.CharField(max_length=32, null=False)
    written_phone = models.CharField(max_length=32, null=False)
    written_cover_letter = models.TextField(null=False)
    vacancy = models.ForeignKey(vacancy_models.Vacancy, on_delete=models.CASCADE, related_name='application_vacancy')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application_user')


class Resume(models.Model):
    JUNIOR = 'JR'
    MIDDLE = 'MD'
    SENIOR = 'SR'
    LEAD = 'LD'
    GRADE_CHOICES = [
        (JUNIOR, 'Джуниор'),
        (MIDDLE, 'Миддл'),
        (SENIOR, 'Синьор'),
        (LEAD, 'Лид')
    ]

    NOT_INTERESTED = 'NI'
    INTERESTED = 'IN'
    IN_SEARCH = 'IS'
    STATUS_CHOICES = [
        (NOT_INTERESTED, 'Не ищу работу'),
        (INTERESTED, 'Рассматриваю предложения'),
        (IN_SEARCH, 'Ищу работу')
    ]

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NOT_INTERESTED)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='resume')
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=32, null=False)
    salary = models.IntegerField()
    specialty = models.ForeignKey(vacancy_models.Specialty, on_delete=models.CASCADE, related_name='resume')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default=JUNIOR)
    education = models.TextField(max_length=128)
    experience = models.TextField(max_length=256)
    portfolio = models.URLField()

from django.db import models
from django.contrib.auth.models import User

import vacancies.models as vacancy_models


class Application(models.Model):
    written_username = models.CharField(max_length=64, null=False)
    written_phone = models.CharField(max_length=32, null=False)
    written_cover_letter = models.TextField(null=False)
    vacancy = models.ForeignKey(vacancy_models.Vacancy, on_delete=models.CASCADE, related_name='application')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application')

from django.forms import forms, ModelForm
import vacancies.models as vacancies_models
import account.models as account_models

from django.contrib.auth.forms import UserCreationForm


class VacancyForm(ModelForm):
    class Meta:
        model = vacancies_models.Vacancy
        fields = '__all__'


class ResumeForm(ModelForm):
    class Meta:
        model = account_models.Resume
        fields = '__all__'


class ApplicationForm(ModelForm):
    class Meta:
        model = account_models.Application
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = vacancies_models.Company
        # fields = '__all__'
        exclude = ['logo']
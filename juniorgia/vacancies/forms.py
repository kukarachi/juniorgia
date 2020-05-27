from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Company, Vacancy


class SearchForm(forms.Form):
    data = forms.CharField(max_length=128)


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = '__all__'


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        # fields = '__all__'
        exclude = ['height_field', 'width_field']

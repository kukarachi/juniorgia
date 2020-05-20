from django.forms import forms, ModelForm
import vacancies.models as my_models


class CompanyForm(ModelForm):
    class Meta:
        model = my_models.Company
        # fields = '__all__'
        exclude = ['logo']


class VacancyForm(ModelForm):
    class Meta:
        model = my_models.Vacancy
        fields = '__all__'

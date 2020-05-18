from django.forms import forms, ModelForm
import vacancies.models as my_models


class CreateCompanyForm(ModelForm):
    class Meta:
        model = my_models.Company
        fields = '__all__'


class CreateVacancyForm(ModelForm):
    class Meta:
        model = my_models.Vacancy
        fields = '__all__'

from django.forms import ModelForm

import account.models as account_models


class ResumeForm(ModelForm):
    class Meta:
        model = account_models.Resume
        fields = '__all__'


class ApplicationForm(ModelForm):
    class Meta:
        model = account_models.Application
        fields = '__all__'

from django.shortcuts import render
from django.views import View


from account.forms import CreateCompanyForm, CreateVacancyForm
from vacancies.models import Company, Specialty, Vacancy

from django.contrib.auth.forms import UserCreationForm



class CompanyCreate(View):
    form_class = CreateCompanyForm
    success_url = '/'
    template_name = 'account/company-edit.html'


class MyVacancies(View):
    def get(self, request, id):
        pass


class MyCompanyView(View):
    def get(self, request):
        my_company = Company.objects.filter(owner=request.user).first()
        print(my_company)

        if my_company:
            path_to_file = 'account/company-edit.html'
        else:
            path_to_file = 'account/company-create.html'

        context = {'company': my_company, 'form': CreateCompanyForm}
        return render(request, path_to_file, context)

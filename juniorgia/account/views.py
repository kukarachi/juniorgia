from django.shortcuts import render, redirect
from django.views import View


from account.forms import CompanyForm, VacancyForm
from vacancies.models import Company, Specialty, Vacancy
from django.views.generic import CreateView
from django.contrib import messages


class CompanyCreate(CreateView):
    form_class = CompanyForm
    template_name = 'account/company-edit.html'

    def get(self, request):
        if Company.objects.filter(owner=request.user).first():
            return redirect('/account/mycompany')

        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        data = request.POST.dict()
        data['owner'] = request.user
        form = self.form_class(data)

        print('User:', request.user)
        print('Errors:', form.errors)

        if form.is_valid():
            form.save()
            return redirect('/account/mycompany')

        return render(request, self.template_name, {'form': form})


class MyVacanciesView(View):
    def get(self, request, id):
        pass


class VacancyCreate(CreateView):


    def post(self):
        pass


class MyCompanyView(View):
    def get(self, request):
        my_company = Company.objects.filter(owner=request.user).first()
        form = CompanyForm()

        if my_company:
            form = CompanyForm(instance=my_company)
            path_to_file = 'account/company-edit.html'
        else:
            path_to_file = 'account/company-create.html'
        context = {'company': my_company, 'form': form}
        return render(request, path_to_file, context)

    def post(self, request):
        my_company = Company.objects.filter(owner=request.user).first()

        data = request.POST.dict()
        data['owner'] = request.user
        message = None
        form = CompanyForm(data, instance=my_company)
        if form.is_valid():
            form.save()
            message = 'Информация была обновлена'

        return render(request, 'account/company-edit.html', {'form': form, 'message': message})

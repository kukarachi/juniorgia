from datetime import date

from account.forms import CompanyForm, VacancyForm, ResumeForm
from account.models import Resume
from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from vacancies.models import Company, Vacancy

from .models import Application


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
        form = self.form_class(data, request.FILES)

        print('User:', request.user)
        print('Errors:', form.errors)

        if form.is_valid():
            form.save()
            return redirect('/account/mycompany')

        return render(request, self.template_name, {'form': form})


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


class MyVacanciesView(View):
    def get(self, request):
        my_company = Company.objects.filter(owner=request.user).first()
        if not my_company:
            return redirect('/account/mycompany')

        my_vacancies_list = Vacancy.objects.filter(company=my_company).values().annotate(
            applications_count=Count('application_vacancy'))

        print(my_vacancies_list)

        if len(my_vacancies_list) > 0:
            path_to_file = 'account/vacancy-list.html'

        else:
            path_to_file = 'account/vacancy-create.html'

        return render(request, path_to_file, {'vacancies': my_vacancies_list})


class MyVacancyView(View):
    form_class = VacancyForm
    template_name = 'account/vacancy-edit.html'

    def get(self, request, id):
        vacancy = Vacancy.objects.get(id=id)
        form = self.form_class(instance=vacancy)

        applications = Application.objects.filter(vacancy__id=id)
        return render(request, self.template_name, {'form': form, 'applications': applications})

    def post(self, request, id):
        instance = Vacancy.objects.get(id=id)
        data = request.POST.dict()
        data['company'] = Company.objects.get(owner=request.user)
        data['published_at'] = date.today()
        form = self.form_class(data, instance=instance)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, {'message': 'Вакансия обновлена', 'form': form})


class VacancyCreate(FormView):
    form_class = VacancyForm
    template_name = 'account/vacancy-edit.html'
    success_url = '/account/mycompany/vacancies'

    def post(self, request):
        data = request.POST.dict()
        data['company'] = Company.objects.get(owner=request.user)
        data['published_at'] = date.today()
        form = self.form_class(data)

        if form.is_valid():
            form.save()

        return redirect(self.success_url)


class ResumeCreate(View):
    form_class = ResumeForm
    template_name = 'account/resume-edit.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        data = request.POST.dict()
        data['user'] = request.user

        form = self.form_class(data)
        if form.is_valid():
            form.save()
            return redirect('/account/resume')

        return render(request, self.template_name, {'form': self.form_class})


class MyResumeView(View):
    def get(self, request):
        instance = Resume.objects.filter(user=request.user).first()
        form = None
        if instance:
            path_to_file = 'account/resume-edit.html'
            form = ResumeForm(instance=instance)
        else:
            path_to_file = 'account/resume-create.html'

        return render(request, path_to_file, {'form': form})

    def post(self, request):
        data = request.POST.dict()
        data['user'] = request.user

        form = ResumeForm(data)
        if form.is_valid():
            form.save()
            message = 'Резюме сохранено'

        return render(request, 'account/resume-edit.html', {'form': form, 'message': message})



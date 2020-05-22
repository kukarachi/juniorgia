from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView

import account.models as account_models
from account.forms import ApplicationForm
from .models import Company, Specialty, Vacancy


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'vacancies/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    redirect_field_name = '/'
    template_name = 'vacancies/login.html'


class MainView(View):
    def get(self, request):
        companies = Company.objects.filter()
        categories = Specialty.objects.filter()
        vacancy_count_for_company = []
        vacancy_count_for_category = []

        for c in companies:
            vacancy_count_for_company.append((c, Vacancy.objects.filter(company=c).count()))

        for c in categories:
            vacancy_count_for_category.append((c, Vacancy.objects.filter(specialty=c).count()))

        return render(request, 'vacancies/index.html', {'companies': vacancy_count_for_company,
                                                        'categories': vacancy_count_for_category
                                                        })


class CategoryVacanciesView(View):
    def get(self, request, code):
        vacancies = Vacancy.objects.filter(specialty__code=code)
        specialty = get_object_or_404(Specialty, code=code).title
        path_to_file = 'vacancies/vacancies.html'
        context = {'vacancies': vacancies, 'specialty': specialty}

        return render(request, path_to_file, context)


class VacancyIdView(View):
    path_to_file = 'vacancies/vacancy.html'

    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        context = {'vacancy': vacancy, 'form': ApplicationForm}
        return render(request, self.path_to_file, context)

    def post(self, request, id):
        print('IN POST')
        instance = account_models.Application.objects.filter(vacancy__id=id, user=request.user).first()
        print('1')
        data = request.POST.dict()
        data['user'] = request.user
        data['vacancy'] = Vacancy.objects.get(id=id)

        form = ApplicationForm(data, instance=instance)
        print('2')
        print(form.errors)
        if form.is_valid():
            form.save()
            print('3')
            return redirect('/sent')
        print('4')
        return render(request, self.path_to_file, {'form': form})


class SentView(View):
    def get(self, request):
        referrer = request.META['HTTP_REFERER']
        return render(request, 'vacancies/sent.html', {'referrer': referrer})


class VacanciesView(View):
    def get(self, request):
        path_to_file = 'vacancies/vacancies.html'
        context = {'vacancies': Vacancy.objects.filter(), 'specialty': 'Все вакансии'}
        return render(request, path_to_file, context)


class CompanyView(View):
    def get(self, request, id):
        company = get_object_or_404(Company, id=id)
        vacancies = Vacancy.objects.filter(company=company)
        return render(request, 'vacancies/company.html', {'company': company, 'vacancies': vacancies})

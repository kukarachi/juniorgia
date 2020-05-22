import account.models as account_models
from account.forms import ApplicationForm
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import SearchForm, CustomCreationForm
from .models import Company, Specialty, Vacancy


class MySignupView(CreateView):
    form_class = CustomCreationForm
    success_url = '/login'
    template_name = 'vacancies/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    redirect_field_name = '/'
    template_name = 'vacancies/login.html'


class MainView(View):
    def get(self, request):
        # if '.values().' is added between all() and annotate, pictures aren't loaded on template. Interesting.
        categories = Specialty.objects.all().annotate(count=Count('vacancy_specialty'))
        companies = Company.objects.all().annotate(count=Count('vacancy_company'))

        return render(request, 'vacancies/index.html', {'companies': companies,
                                                        'categories': categories,
                                                        'form': SearchForm,
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
        if not request.user.is_authenticated():
            return redirect('/login')

        instance = account_models.Application.objects.filter(vacancy__id=id, user=request.user).first()
        data = request.POST.dict()
        data['user'] = request.user
        data['vacancy'] = Vacancy.objects.get(id=id)

        form = ApplicationForm(data, instance=instance)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('/sent')

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


class SearchView(View):
    def get(self, request):
        key_words = request.GET['data']
        vacancies = Vacancy.objects.filter(skills__contains=key_words)
        return render(request, 'vacancies/search.html', {'form': SearchForm, 'vacancies': vacancies})

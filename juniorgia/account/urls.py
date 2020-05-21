from django.urls import path, re_path
from .views import MyCompanyView, MyVacanciesView, CompanyCreate, VacancyCreate, MyVacancyView, ResumeCreate, \
    MyResumeView

urlpatterns = [
    path('mycompany/', MyCompanyView.as_view()),
    path('mycompany/create', CompanyCreate.as_view()),
    path('mycompany/vacancies/', MyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:id>', MyVacancyView.as_view(), name='my_vacancy'),
    path('mycompany/vacancies/create', VacancyCreate.as_view()),
    path('resume/', MyResumeView.as_view()),
    path('resume/create/', ResumeCreate.as_view()),
]

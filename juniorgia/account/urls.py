from django.urls import path, re_path
from .views import MyCompanyView, MyVacanciesView, CompanyCreate


urlpatterns = [
    path('mycompany/', MyCompanyView.as_view()),
    path('mycompany/create', CompanyCreate.as_view()),
    re_path(r'^mycompany/vacancies/?(?P<id>\d*)?/$', MyVacanciesView.as_view()),
]

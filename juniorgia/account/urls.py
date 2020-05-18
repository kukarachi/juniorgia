from django.urls import path, re_path
from .views import MyCompanyView, MyVacancies


urlpatterns = [
    path('mycompany/', MyCompanyView.as_view()),
    re_path(r'^mycompany/vacancies/?(?P<id>\d*)?/$', MyVacancies.as_view()),
]

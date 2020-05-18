from .models import Company, Specialty, Vacancy
from django.contrib.auth.models import User

jobs = [

    {"title": "Разработчик на Python", "cat": "backend", "company": "staffingsmarter", "salary_from": "100000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик в проект на Django", "cat": "backend", "company": "swiftattack", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Разработчик на Swift в аутсорс компанию", "cat": "backend", "company": "swiftattack",
     "salary_from": "120000", "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Мидл программист на Python", "cat": "backend", "company": "workiro", "salary_from": "80000",
     "salary_to": "90000", "posted": "2020-03-11", "desc": "Потом добавим"},
    {"title": "Питонист в стартап", "cat": "backend", "company": "primalassault", "salary_from": "120000",
     "salary_to": "150000", "posted": "2020-03-11", "desc": "Потом добавим"}

]

""" Компании """

companies = [

    {"title": "workiro"},
    {"title": "rebelrage"},
    {"title": "staffingsmarter"},
    {"title": "evilthreat h"},
    {"title": "hirey "},
    {"title": "swiftattack"},
    {"title": "troller"},
    {"title": "primalassault"}

]

""" Категории """

specialties = [

    {"code": "frontend", "title": "Фронтенд"},
    {"code": "backend", "title": "Бэкенд"},
    {"code": "gamedev", "title": "Геймдев"},
    {"code": "devops", "title": "Девопс"},
    {"code": "design", "title": "Дизайн"},
    {"code": "products", "title": "Продукты"},
    {"code": "management", "title": "Менеджмент"},
    {"code": "testing", "title": "Тестирование"}

]

#################### make db empty ##################
Specialty.objects.filter().delete()
Company.objects.filter().delete()
Vacancy.objects.filter().delete()
#####################################################
print('erased everything')


User.objects.create_superuser(username='super_ragim', password='Qwertygang2002')
User.objects.create_user(username='ragim', password='Qwertygang2002')

owner = User.objects.get_by_natural_key(username='ragim')

for spec in specialties:
    Specialty.objects.create(code=spec['code'], title=spec['title'], picture="https://place-hold.it/100x60")

for c in companies:
    Company.objects.create(name=c['title'], logo="https://place-hold.it/100x60", owner=owner)

for job in jobs:
    company = Company.objects.get(name=job['company'])
    spec = Specialty.objects.get(code=job['cat'])
    Vacancy.objects.create(title=job['title'], specialty=spec, company=company, description=job['desc'],
                           salary_min=job['salary_from'], salary_max=job['salary_to'], published_at=job['posted'])

print('loaded new data')

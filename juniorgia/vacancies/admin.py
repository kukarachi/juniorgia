from .models import Specialty, Company
from django.contrib import admin


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class CompanyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Specialty, SpecialtyAdmin)

admin.site.register(Company, CompanyAdmin)

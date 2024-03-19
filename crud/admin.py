from django.contrib import admin
from crud.models import Beer, Employeeinfo


class BeerAdmin(admin.ModelAdmin):
    list_display = ['name', 'taste', 'color', 'price']


admin.site.register(Beer,BeerAdmin)


class EmployyeinfoAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'emp_name', 'emp_sal', 'emp_addr']


admin.site.register(Employeeinfo,EmployyeinfoAdmin)

from django.contrib import admin
from secondapp.models import Student, User, College, Company, Worker


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno', 'name', 'fee', 'addr']


admin.site.register(Student, StudentAdmin)

admin.site.register(User)


class CollegeAdmin(admin.ModelAdmin):
    list_display = ['college_name', 'branch', 'id_number', 'fee']


admin.site.register(College, CollegeAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'ceo']


admin.site.register(Company, CompanyAdmin)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ['eno', 'name', 'salary', 'company']


admin.site.register(Worker, WorkerAdmin)





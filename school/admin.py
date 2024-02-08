from django.contrib import admin

from school.models import *


@admin.register(School)
@admin.register(SchoolSerie)
@admin.register(SchoolClass)
@admin.register(Employee)
@admin.register(Student)
@admin.register(Schoolroom)
@admin.register(SchoolSubjects)
@admin.register(Classroom)
@admin.register(PresenceInClass)
@admin.register(TestScore)
class UserAdmin(admin.ModelAdmin):
    ...
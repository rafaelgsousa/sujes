from django.contrib import admin

from persons.models import *


@admin.register(CustomUser)
@admin.register(Phone)
@admin.register(Role)
class UserAdmin(admin.ModelAdmin):
    ...
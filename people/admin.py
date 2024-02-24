from django.contrib import admin

from people.models import *


@admin.register(CustomUser)
@admin.register(Phone)
@admin.register(VerificationCode)
@admin.register(Logger)
class UserAdmin(admin.ModelAdmin):
    ...
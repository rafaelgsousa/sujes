from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import *

app_name = 'users'

view_customeusers = SimpleRouter()
view_customeusers.register('', CustomUserView, basename='users-router')

urlpatterns = [
    path('', include(view_customeusers.urls))
]
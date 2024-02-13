from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = 'users'

view_customeusers = SimpleRouter()
view_customeusers.register('', CustomUserView, basename='users-router')

urlpatterns = [
    path('persons/', include(view_customeusers.urls)),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
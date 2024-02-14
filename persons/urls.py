from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

app_name = 'users'

view_customeusers = SimpleRouter()
view_customeusers.register('', CustomUserView, basename='users-router')

view_role = SimpleRouter()
view_role.register('', RoleView, basename='role-router')

view_phone = SimpleRouter()
view_phone.register('', PhoneView, basename='phone-router')

urlpatterns = [
    path('persons/', include(view_customeusers.urls)),
    path('role/', include(view_role.urls)),
    path('phone/', include(view_phone.urls)),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
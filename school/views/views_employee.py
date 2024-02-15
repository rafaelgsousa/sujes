from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils import ListPagination

from ..serializers import *


# Create your views here.
class EmployeeView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = EmployeeSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
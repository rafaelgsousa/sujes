from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils import ListPagination

from ..serializers import *


# Create your views here.
class EstudentView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
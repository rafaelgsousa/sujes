from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from permissions import *
from utils import ListPagination

from ..serializers import *


class SchoolView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    serializer_class = SchoolSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = School.objects.all()

class SchoolSerieView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = SchoolSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = SchoolSerie.objects.all()

class SchoolClassView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = SchoolClassSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = SchoolClass.objects.all()

class SchoolroomView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = SchoolroomSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Schoolroom.objects.all()

class SchoolSubjectsView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = SchoolSubjectsSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = SchoolSubject.objects.all()

class ClassroomView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = ClassroomSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Classroom.objects.all()

class PresenceInClassView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = PresenceInClassSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = PresenceInClass.objects.all()

class TestScoreView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = TestScoreSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = TestScore.objects.all()

class BookView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = BookSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Book.objects.all()

class RentedView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , CheckPermissions]
    pagination_class = ListPagination
    serializer_class = RentedSerializer
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Rented.objects.all()
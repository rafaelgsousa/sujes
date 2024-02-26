from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import Group, Permission
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from permissions import *
from utils import ListPagination

from ..serializers import *


class CustomUserView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , DjangoModelPermissions]
    serializer_class = CustomUserSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action in ['login']:
            return []
        else:
            return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = get_object_or_404(CustomUser,email=email)
        
        user_serialize = CustomUserSerializer(instance=user)

        if user_serialize.data['login_erro'] >= 3:
            raise PermissionDenied(detail='error: Account blocked due to excessive login errors. Contact an administrator.')
        
        if not user.is_active:
            raise PermissionDenied(detail='error: User is inactive.')

        if check_password(password, user.password):

            token = RefreshToken.for_user(user)

            if user.login_erro > 0:
                user.login_erro = CustomUser.LoginError.ZERO
                user.save(update_fields=list(['login_erro']))

            return Response(
                {
                    'token': {
                        'access': str(token.access_token),
                        'refresh': str(token), 
                    },
                    'user': CustomUserSerializer(user).data
                },
                status=status.HTTP_200_OK
            )
        else:
            user.login_erro += 1
            user.save(update_fields=list(['login_erro']))

            if user.login_erro >= 3:
                raise PermissionDenied(detail='error: Account blocked due to excessive login errors. Contact an administrator.')
            else:
                return Response(
                    {
                        'error': 'Incorrect password or email. Three login errors lead to account lockout'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(CustomUser, pk=request.user.id)
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {
                    'user': user.email,
                    'message': 'logout'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

class GroupView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , DjangoModelPermissions]
    serializer_class = GroupSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Group.objects.all()
    
    def create(self, request, *args, **kwargs):
        body = request.data

        permissions = Permission.objects.all()

        list_permissions = []

        for modeltype in body.get('permissions', []):
            for permissiontype in modeltype.get('permissions', []):
                permission_codename = f'{permissiontype}_{modeltype['name']}'
                matching_permission = next((permission for permission in permissions if permission.codename == permission_codename), None)
                if matching_permission:
                    list_permissions.append(matching_permission.id)

        group_data = {
            'name': body.get('name'),
            'permissions': list_permissions
        }

        serializer = GroupSerializer(data=group_data)
        
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'group': serializer.data}, status=status.HTTP_201_CREATED)



class PhoneView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , DjangoModelPermissions]
    serializer_class = PhoneSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
    queryset = Phone.objects.all()


class LoggerView(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , ReadOnly]
    serializer_class = LoggerSerializer
    pagination_class = ListPagination
    http_method_names = ['get', 'options', 'head']
    queryset = Logger.objects.all()
import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.urls import resolve
from rest_framework.response import Response

from persons.models import CustomUser, Logger
from utils import change_to_dict_del_some_fields, get_value_for_key

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            request_body = request.body
            response = self.get_response(request)

            user_id, email, body, view_name = self.extract_request_data(request, response, request_body)
            self.log_request_data(request, user_id, email, body, view_name, response)

        except json.JSONDecodeError as e:
            logger.error(f'Error decoding request JSON: {e}')
            return JsonResponse({'error': 'Invalid JSON format in request body.'}, status=400)

        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return JsonResponse({'error': 'Unexpected error'}, status=500)

        return response

    def extract_request_data(self, request, response, request_body):
        user_id = None
        email = ''
        body = None
        view_name = ''
        method = request.method
        path = request.path

        user_id = request.user.id if request.user else None
        
        if not user_id and isinstance(response, Response):
            print('1')
            user_id = get_value_for_key(response.data, 'id')
            email = get_value_for_key(response.data, 'email') if not user_id else None
            print('1 - 2')

        if not user_id and not email and isinstance(response, Response):
            print('2')
            user_id = get_value_for_key(request.resolver_match.kwargs, 'pk')
            email = get_value_for_key(request.resolver_match.kwargs, 'email')
            email = get_value_for_key(json.loads(request_body.decode('utf-8')), 'email') if not email and len(request_body.decode('utf-8')) else email
            print('2 - 2')

        if not user_id and not email and isinstance(response, JsonResponse):
            print('3')
            user_id = get_value_for_key(resolve(request.path).kwargs,'pk')
            email = get_value_for_key(resolve(request.path).kwargs,'email') if not user_id else None
            print('3 - 2')


        if hasattr(request, 'resolver_match') and request.resolver_match:
            print('4')
            view_name = request.resolver_match.url_name
            print('4 - 2')


        if isinstance(request_body, bytes) and 'admin' in path:
                print('5')
                body = request_body.decode('utf-8')
                print(f'body = {body}')
                body = change_to_dict_del_some_fields(body) if body else body
                print('5 - 2')


        elif method == 'POST' and 'logout' in path:
            print('6')
            body = None    
            print('6 - 2')        
            
        elif request_body:
                print('7')
                body = json.loads(request_body.decode('utf-8'))
                print('7 - 2') 
        

        return user_id, email, body, view_name

    def log_request_data(self, request, user_id, email, body, view_name, response):
        try:
            user = None

            if user_id:
                user = CustomUser.objects.filter(id=user_id).first()

            if not user and email:
                user = CustomUser.objects.filter(email=email).first()

            if user:
                if body and not isinstance(body, str) and 'password' in body:
                    del body['password']

                Logger.objects.create(
                    endpoint=request.path,
                    user=user,
                    method=request.method,
                    body=str(body),
                    view=view_name,
                    status=response.status_code,
                )
            else:
                logger.error('User not found.')
                return JsonResponse({'error': 'User not found.'}, status=404)
        except ObjectDoesNotExist:
            logger.error('User not found.')
            return JsonResponse({'error': 'User not found.'}, status=404)
        except Exception as e:
            logger.error(f'Error getting user: {e}')
            return JsonResponse({'error': 'Error getting user.'}, status=500)
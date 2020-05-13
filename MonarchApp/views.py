from django.shortcuts import render
from .models import users
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .API.UserAuthentication import user_auth
from django.db import *

from django.core.exceptions import *
# Create your views here.

@api_view(['POST'])
def user_login(request):
    try:
        if request.method == 'POST':
            req_data = request.data
            print("printing input json as req_data ",req_data)
            if not req_data:
                raise EmptyResultSet
            if not req_data.get("email") or not req_data.get("password"):
                raise DataError
            email = req_data.get("email")
            password = req_data.get("password")
            # user_exists = user_info.objects.get(email)
            output_json = user_auth(req_data)
            if output_json:
                return JsonResponse(output_json, safe=False)
            else:
                raise DataError

    except DataError:
        output_json = {"value":"Errorss"}
        return JsonResponse(output_json,safe=False)








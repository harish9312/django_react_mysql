# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from django.db import connection  

from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class SaveUser(APIView):

    def post(self, request, format=None):
        try:
            userName = request.data['userName']
            password = request.data['password']
            email = request.data['email']
            phoneNo = request.data['phoneNo']
            args = (userName, password, email, phoneNo)
            cursor = connection.cursor()
            cursor.callproc('cgjs_SaveUser' , args)
            return Response({'StatusCode':'200', 'message':'User ' + userName + ' Created Successfully'})
        except:
            return Response({'StatusCode': '201', 'message': 'Something Went wrong...!!'})
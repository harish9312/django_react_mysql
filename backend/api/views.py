# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import generics
from django.db import connection  

from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import UserSerializer
from django.core import serializers

# Create your views here.

class SaveUser(APIView):

    def post(self, request, format=None):
        try:
            userName = request.data['userName']
            password = request.data['password']
            email = request.data['email']
            phoneNo = request.data['phoneNo']
            # data = User.objects.get(userName= userName)
            # print(data)
            user = User(userName = userName, password = password, email = email, phoneNo = phoneNo)
            user.save()
            return Response({'StatusCode':'200', 'message':'User ' + userName + ' Created Successfully'})
        except:
            return Response({'StatusCode': '201', 'message': 'Username or email already exist..!!!'})

class LoginUser(APIView):

    def post(self, request, format=None):
        try:
            userName = request.data['userName']
            password = request.data['password']
            data = User.objects.get(userName= userName, password = password)
            serialized_obj = serializers.serialize('json', [data])
            return Response({'StatusCode':'200', 'message': 'Login Successfull'})
        except:
            return Response({'StatusCode':'403', 'message': 'Invalid Username or Password...!!!'})

class LoginUser(APIView):

    def post(self, request, format=None):
        try:
            userName = request.data['userName']
            password = request.data['password']
            data = User.objects.get(userName= userName, password = password)
            serialized_obj = serializers.serialize('json', [data])
            return Response({'StatusCode':'200', 'message': 'Login Successfull'})
        except:
            return Response({'StatusCode':'403', 'message': 'Invalid Username or Password...!!!'})

class GetUsers(APIView):

    def get(self, request, format=None):
        # try:
            rows = User.objects.values_list()
            print(rows)
            responseJSON = []
            for data in rows:
                d = {}
                d['userName'] = data[0]
                d['email'] = data[2]
                d['phoneNo'] = data[3]
                responseJSON.append(d)
            return Response({'StatusCode':'200', 'message': responseJSON})
        # except:
            # return Response({'StatusCode':'403', 'message': 'Invalid Username or Password...!!!'})
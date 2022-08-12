from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import permissions

from ..serializers.customerSerializer import CustomerSerializer
from ..models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import mixins

  



  
@api_view(['POST'])
def createCustomer(request,name,email):
    if name and email:
        try:
            newCustomer = Customer(name=name,email=email)
            newCustomer.save()
            res = "Customer Created!"

        except:
            res = "Customer Already Exists!"
    return Response({"Attention": res})






######## View Customer ########
@api_view(['GET'])
def CustomerView(request,email):
    if email:
        try:
            customers = Customer.objects.filter(email=email)
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        except customers.DoesNotExist:
            raise Http404

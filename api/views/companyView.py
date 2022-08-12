from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import permissions

from ..serializers.companySerializer import CompanySerializer
from ..models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import mixins

  



  
@api_view(['POST'])
def createCompany(request,companyName,companyEmail):
    if companyName and companyEmail:
        try:
            newCompany = Company(companyName=companyName,comppanyEmail=companyEmail)
            newCompany.save()
            res = "Company Created!"

        except:
            res = "Company Already Exists!"
    return Response({"Attention": res})






######## View Customer ########
@api_view(['GET'])
def CompanyView(request,companyEmail):
    if companyEmail:
        try:
            company = Company.objects.filter(comppanyEmail=companyEmail)
            serializer = CompanySerializer(company, many=True)
            return Response(serializer.data)
        except company.DoesNotExist:
            raise Http404


####### Selec Primary Phone Number #########
@api_view(['POST'])
def createCompany(request,primaryPhone,companyEmail):
    if primaryPhone and companyEmail:
        try:
            company = Company.objects.get(comppanyEmail=companyEmail)
            customer = Customer.objects.filter(company =company, phone_number=primaryPhone).first()
            if customer:
                company.primary_phone_number = primaryPhone
                company.save()
                res = f"Primary Phone {customer.phone_number}!"

        except:
            res = "Phone Number Not Found"
    return Response({"Attention": res})

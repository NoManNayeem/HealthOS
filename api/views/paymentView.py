from .customerView import *
from ..serializers.paymentSerializer import PaymentSerializer
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

  
def get_amount(plan):
    if plan ==1:
        amount = 500
    if plan == 2:
        amount=750
    if plan ==3:
        amount = 1500
    return amount

##### Customer Payment ###########
@api_view(['POST'])
def makeCompanyPayment(request,date,primary_phone,plan):
    if date and primary_phone and plan:
        amount = get_amount(plan)
        company = Company.objects.get(primary_phone_number=primary_phone)
        company.plan=plan
        company.save()
        customers = Customer.objects.filter(company=company)
        for customer in customers:
            customer.plan=plan
            customer.save()
            try:
                newPayment = Payment(date=date, customer = customer, trans_id = "transactionID",amount=amount)
                newPayment.save()
                res = "Payment Created!"

            except:
                res = "Error!"
    return Response({"Attention": res})


##### Customer Payment ###########
@api_view(['POST'])
def makeCustomerPayment(request,date,phoneNumber,plan):
    if date and phoneNumber:
        customer = Customer.objects.get(phone_number=phoneNumber)
        customer.plan=plan
        customer.save()
        try:
            newPayment = Payment(date=date, customer = customer, trans_id = "transactionID",amount=get_amount(plan))
            newPayment.save()
            res = "Payment Created!"

        except:
            res = "Error!"
    return Response({"Attention": res})






######## View Payment ########
@api_view(['GET'])
def PaymentView(request,transactionID):
    if transactionID:
        try:
            payment = Payment.objects.filter(trans_id=transactionID)
            serializer = PaymentSerializer(payment, many=True)
            return Response(serializer.data)
        except payment.DoesNotExist:
            raise Http404

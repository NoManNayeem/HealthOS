from django.urls import path

from .views import customerView,paymentView, companyView, getMoneyFromExAPI, changPlan

urlpatterns = [
    path('customer/Register/name=<str:name>&email=<str:email>/', customerView.createCustomer, name='createCustomer'),
    path('customer/View/email=<str:email>/', customerView.CustomerView, name='customerView'),



    ####### Company URLs ######
    path('company/setPrimaryPhone/primaryPhone=<int:primaryPhone>&companyEmail=<str:companyEmail>/', companyView.createCompany, name='createCompany'),
    path('company/Register/companyName=<str:companyName>&companyEmail=<str:companyEmail>/', companyView.createCompany, name='createCompany'),
    path('company/View/companyEmail=<str:companyEmail>/', companyView.CompanyView, name='companyView'),


    ###### Payment URLs ########
    path('payment/makePayment/date=<str:date>&phoneNumber=<str:phoneNumber>&plan=<int:plan>/', paymentView.makeCustomerPayment, name='MakePayment'),

    path('payment/makeCompanyPayment/date=<str:date>&primary_phone=<str:primary_phone>&plan=<int:plan>/', paymentView.makeCompanyPayment, name='makeCompanyPayment'),
    path('payment/View/transactionID=<str:transactionID>/', paymentView.PaymentView, name='PaymentView'),

    path('payment/GetMoney/merchantInfo=<str:merchantInfo>&amount=<int:amount>/', getMoneyFromExAPI.getPayment, name='Get Money'),

    ###### Change Plan #########
    path('plan/Change/plan=<int:plan>&phoneNumber=<int:phoneNumber>&transaction_id=<str:transaction_id>/', changPlan.changePlan, name='Change Customer Plan'),
    path('plan/ChangeCompanyPlan/plan=<int:plan>&phoneNumber=<int:phoneNumber>&transaction_id=<str:transaction_id>/', changPlan.changePlan, name='Change Company Plan'),

]
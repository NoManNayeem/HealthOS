from .companyView import *


@api_view(['POST'])
def changePlan(request,plan,transaction_id, phoneNumber):
    if plan and transaction_id and phoneNumber:
        customer = Customer.objects.get(phone_number = phoneNumber)
        payment = Payment.objects.get(trans_id=transaction_id)
        if payment:
            customer.plan=plan
            customer.save()
            res = "Subscription Plan Changed"
    else:
        res = "Could not change plan!"
    return Response(res)




@api_view(['POST'])
def changeCompanyPlan(request,plan,transaction_id, primaryPhoneNumber):
    if plan and transaction_id and primaryPhoneNumber:
        company = Company.objects.get(primary_phone_number = primaryPhoneNumber)
        payment = Payment.objects.get(trans_id=transaction_id)
        if company:
            customers = Customer.objects.filter(company=company)
            for customer in customers:
                if payment:
                    customer.plan=plan
                    customer.save()
                    res = "Subscription Plan Changed"
            else:
                res = "Could not change plan!"
    return Response(res)




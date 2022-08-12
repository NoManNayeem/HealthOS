from .customerView import *




##### Customer Payment ###########
@api_view(['GET'])
def getPayment(request,merchantInfo,amount):
    if merchantInfo and amount:
        print(f"External API calls to get money from Merchant Account")
        res = f"${amount} has been transferred to your acoount on {datetime.today()}"
    return Response(res)

from django.contrib import admin
from .models import Company,Customer,Payment
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'plan','primary_phone_number',)
    # list_filter = (
    #     ('company_name', admin.RelatedOnlyFieldListFilter),
    # )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company','plan','phone_number',)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date','deadline','trans_id',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Payment,PaymentAdmin)
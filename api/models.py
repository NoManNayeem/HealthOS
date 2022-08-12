from django.db import models
from datetime import datetime

####### Company Model ########
class Company(models.Model):
    class SubPlan(models.IntegerChoices):
        Bronze = 1, "Globalnet Bronze"
        Silver = 2, "Globalnet Silver"
        Gold= 3, "Globalnet Gold"
    plan = models.PositiveSmallIntegerField(choices=SubPlan.choices, blank=True, null=True, default=None)
    companyName = models.CharField(max_length=100)
    comppanyEmail = models.EmailField(max_length=254, unique=True, blank=True, null=True, default=None)
    primary_phone_number = models.IntegerField(default=None, blank=True, null = True)





########## Customer Model #########
class Customer(models.Model):
    class SubPlan(models.IntegerChoices):
        Bronze = 1, "Globalnet Bronze"
        Silver = 2, "Globalnet Silver"
        Gold= 3, "Globalnet Gold"
    valid = models.BooleanField(default=False)
    assigned = models.BooleanField(default=False)
    plan = models.PositiveSmallIntegerField(choices=SubPlan.choices, blank=True, null=True, default=None)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True, default=None)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None)
    
    # phone number would increment on save/creating new customer || "Default Value" is the starting point.
    # This is a simple starting point, phone numbers can be define in real usage.
    phone_number = models.IntegerField(default=1000000000)

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum/last phone_number value from the database
            last_phone_number = Customer.objects.all().aggregate(largest=models.Max('phone_number'))['largest']
            # aggregate can return None! Check it first.
            # If it isn't none, we will use the last_phone_number specified (which should be the greatest) and add one to it
            if last_phone_number is not None:
                self.phone_number = last_phone_number + 1
        # To save with phone number
        super(Customer, self).save(*args, **kwargs)
    def __str__(self):
         return self.name



    





########## Payment Model #########
class Payment(models.Model):
    date= models.DateField(default=datetime.today)
    deadline = models.DateField(default=datetime.today)
    amount = models.IntegerField(default=0)
    trans_id = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
         return self.customer.name



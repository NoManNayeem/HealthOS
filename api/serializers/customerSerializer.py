from django.contrib.auth.models import User, Group
from rest_framework import serializers
from ..models import Customer,Company,Payment


class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Customer
        fields = "__all__"
from .customerSerializer import *


class PaymentSerializer(serializers.ModelSerializer):
    # user = UserSerializer(many=False)
    class Meta:
        model = Payment
        fields = "__all__"
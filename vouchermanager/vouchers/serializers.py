from rest_framework import serializers
from vouchers.models import Voucher


# Voucher Serializer
class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

from rest_framework import serializers
from vouchers.models import Voucher


# Voucher Serializer
class VoucherSerializer(serializers.ModelSerializer):
    """
    Serializer which only contains code, name, remaining vouchers, and flat/percentage discount fields.
    Remaining vouchers and date creations are automatically generated on voucher generation.
    """
    class Meta:
        model = Voucher
        fields = ['code', 'name', 'flat_off', 'percent_off', 'remaining']

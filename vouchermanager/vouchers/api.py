from vouchers.models import Voucher
from rest_framework import viewsets, permissions
from .serializers import VoucherSerializer


# Voucher Viewset
class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = VoucherSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

from vouchers.models import Voucher
from rest_framework import viewsets, permissions
from .serializers import VoucherSerializer
from django.http import JsonResponse
from rest_framework import status


class VoucherViewSet(viewsets.ModelViewSet):
    """
    VoucherViewSet able to retrieve, submit, insert, and update vouchers.
    """
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    # Only the following HTTP methods are allowed as specified per spec
    http_method_names = ['get', 'post', 'put', 'patch']

    # /api/vouchers/id
    def retrieve(self, request, pk=None):
        """
        Custom retrieve function that decreases the remaining voucher count by 1.
        Returns a custom 422 error if there are no more voucher code uses remaining
        Returns a custom 404 error if voucher code is not found
        """

        try:
            voucher = Voucher.objects.get(pk=pk)
        except Voucher.DoesNotExist:
            # Voucher code not found
            return JsonResponse({'message': 'Invalid Voucher Code'}, status=status.HTTP_404_NOT_FOUND)

        # Decrement the remaining voucher by 1
        if voucher.remaining < 1:
            # No more vouchers remaining
            return JsonResponse({'message': 'This voucher has been completely used'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        voucher.remaining -= 1
        voucher.save()
        voucher_serializer = VoucherSerializer(voucher)
        return JsonResponse(voucher_serializer.data)

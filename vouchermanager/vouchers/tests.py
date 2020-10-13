from vouchers.models import Voucher
from django.test import TestCase
from django.core.exceptions import ValidationError


class VoucherTestCase(TestCase):
    """
    Various test cases to test logical and database integrity
    """

    def setup(self):
        """
        Simple initial setup which involves creating a single voucher object
        """
        test_coupon = Voucher.objects.create(
            code="1234", name="testcoupon1", flat_off=42)

    def flat_and_percent_case(self):
        """
        Case - If both flat and percentage discounts are added.
        A ValidationError is expected to be raised as these two can not be added together
        """
        try:
            invalid_voucher = Voucher.objects.create(code="4215", name="testcoupon2",
                                                     flat_off=10, percent_off=50)
        except ValidationError as msg:
            self.assertTrue(
                'Voucher can only be percentage based or flat rate based but not both.' in msg)

    def no_discount(self):
        """
        Case - If no percentage/flat discounts are added.
        A ValidationError is expected to be raised as one of these must not be blank/null 
        """
        try:
            invalid_voucher = Voucher.objects.create(
                code="4215", name="testcoupon2")
        except ValidationError as msg:
            self.assertTrue(
                'A flat or percentage discount is required by the voucher.' in msg)

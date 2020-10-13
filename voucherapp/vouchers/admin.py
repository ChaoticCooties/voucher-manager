from django.contrib import admin
from .models import Voucher

"""
Admin site which is connected to the Voucher model.
"""
admin.site.register(Voucher)

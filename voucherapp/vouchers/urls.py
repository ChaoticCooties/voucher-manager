from rest_framework import routers
from .views import VoucherViewSet

"""
Default router which routes acording to the VoucherViewSet to /api/vouchers
"""

router = routers.DefaultRouter()
router.register('api/vouchers', VoucherViewSet, 'vouchers')

urlpatterns = router.urls

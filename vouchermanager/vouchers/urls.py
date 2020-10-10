from rest_framework import routers
from .api import VoucherViewSet

router = routers.DefaultRouter()
router.register('api/vouchers', VoucherViewSet, 'vouchers')

urlpatterns = router.urls

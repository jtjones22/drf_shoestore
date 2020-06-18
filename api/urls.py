from django.conf.urls import include, url
from rest_framework import routers

from api.views import (
    ShoeViewSet,
    ShoeColorViewSet,
    ShoeTypeViewSet,
    ManufacturerViewSet,
)

router = routers.DefaultRouter()

router.register(r'shoe', ShoeViewSet)
router.register(r'shoe_color', ShoeColorViewSet)
router.register(r'shoe_type', ShoeTypeViewSet)
router.register(r'manufacturer', ManufacturerViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]

from rest_framework.viewsets import ModelViewSet

from api.serializer import (
    ShoeSerializer,
    ShoeColorSerializer,
    ShoeTypeSerializer,
    ManufacturerSerializer
    )

from shoe_data.models import (
    Shoe,
    ShoeColor,
    ShoeType,
    Manufacturer,
)
# Create your views here.


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = Shoe.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeType.objects.all()


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()

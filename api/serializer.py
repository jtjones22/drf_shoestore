from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer
    )
from shoe_data.models import Shoe, ShoeColor, ShoeType, Manufacturer


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = (
            'id',
            'color_name',
        )


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = (
            'id',
            'style',
        )


class ManufacturerSerializer(ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = (
            'id',
            'name',
            'website',
        )


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'id',
            'size',
            'brand',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        )

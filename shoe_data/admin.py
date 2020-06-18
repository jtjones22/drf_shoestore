from django.contrib import admin
from shoe_data.models import ShoeColor, Shoe, ShoeType, Manufacturer

admin.site.register(ShoeColor)
admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(Manufacturer)

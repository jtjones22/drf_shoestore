from django.core.management.base import BaseCommand
from shoe_data.models import ShoeType, ShoeColor


class Command(BaseCommand):

    def handle(self, *args, **options):
        shoe_styles = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other',
        ]
        shoe_colors = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black',
        ]
        for style in shoe_styles:
            ShoeType.objects.create(
                style=style
            )

        for color in shoe_colors:
            ShoeColor.objects.create(
                color_name=color
            )

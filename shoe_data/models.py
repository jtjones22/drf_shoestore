from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=250)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    COLOR_NAME_CHOICES = [
        ('red', 'Red'),
        ('orange', 'Orange'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('indigo', 'Indigo'),
        ('violet', 'Violet'),
        ('white', 'white'),
        ('black', 'Black'),
    ]
    color_name = models.CharField(
        max_length=15,
        choices=COLOR_NAME_CHOICES
    )

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)


# Fun Fact of Joe's upbringing in the African Savanna.
# Joe had a pet Rhino named Tank

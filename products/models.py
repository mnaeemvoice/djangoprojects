from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pigeon', 'Pigeon'),
        ('parrot', 'Parrot'),
        ('other', 'Other Products'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('mobile', 'Mobile'),
        ('fashion', 'Fashion'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()

    def __str__(self):
        return self.name
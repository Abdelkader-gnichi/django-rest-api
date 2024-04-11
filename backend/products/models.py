from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=25, blank=True, null=True)
    content = models.TextField(max_length=100, blank=True,null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=55.75)

    def __str__(self):
        return self.title
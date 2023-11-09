from django.db import models

# Create your models here.
<<<<<<< Updated upstream

class Details(models.Model):
    product_id = models.CharField(max_length = 20, default = '', null = False)
    product_name = models.CharField(max_length = 225, default = '', null = False)
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    amount = models.FloatField(max_length = 20, default = '', null = False)
    status_id = models.IntegerField(max_length = 20, default = '', null = True)

class Unit(models.Model):
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    unit_name = models.CharField(max_length = 225, default = '', null = False)    


=======
class StockItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
>>>>>>> Stashed changes

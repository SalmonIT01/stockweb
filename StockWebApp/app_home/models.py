from django.db import models

# Create your models here.

class Details(models.Model):
    product_id = models.CharField(max_length = 20, default = '', null = False)
    product_name = models.CharField(max_length = 20, default = '', null = False)
    unit_id = models.CharField(max_length = 20, default = '', null = False)
    amount = models.CharField(max_length = 20, default = '', null = False)
    status_id = models.IntegerField(max_length = 20, default = '', null = False)

class Unit(models.Model):
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    unit_name = models.CharField(max_length = 225, default = '', null = False)    



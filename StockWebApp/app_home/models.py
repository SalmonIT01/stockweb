from django.db import models

# Create your models here.

class Details(models.Model):
    product_id = models.CharField(max_length = 20, default = '', null = False)
    product_name = models.CharField(max_length = 20, default = '', null = False) 
    product_code = models.CharField(max_length = 20, default = '', null = False) 
from django.db import models

# Create your models here.

class Details(models.Model):
    product_id = models.CharField(max_length = 20, default = '', null = False)
    product_name = models.CharField(max_length = 225, default = '', null = False)
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    amount = models.FloatField(max_length = 20, default = '', null = False)
<<<<<<< HEAD
    status_id = models.IntegerField(max_length = 20, default = '0', null = True)
=======
    status_id = models.IntegerField(max_length = 20, default = '', null = True)
>>>>>>> 612d46bd91d005703dd5df0ab42c1fcf2617ca6a

class Unit(models.Model):
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    unit_name = models.CharField(max_length = 225, default = '', null = False)    



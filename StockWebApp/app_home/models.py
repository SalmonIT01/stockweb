from django.db import models

# Create your models here.

class Details(models.Model):
    product_id = models.CharField(max_length = 30, default = '', null = False,unique=True)
    product_name = models.CharField(max_length = 225, default = '', null = False)
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null = True)
    amount = models.FloatField(max_length = 20, default = '', null = False)
    status_id = models.IntegerField(max_length = 20, default = '', null = True)

class Unit(models.Model):
    unit_id = models.IntegerField(max_length = 20, default = '', null = False)
    unit_name = models.CharField(max_length = 225, default = '', null = False)  
    
# class member(models.Model):
#     m_id = models.AutoField(primary_key=True)
#     m_name = models.CharField(max_length=125,null=True)
#     m_phone = models.CharField(max_length=50,null=True)
#     products_set = models.ManyToManyField('Details')
    
    # def __str__(self):
    #     return self.m_user
    
class borrow_products(models.Model):
    borrow_date = models.DateField(auto_now=False, auto_now_add=False)
    return_date = models.DateField(auto_now=False, auto_now_add=False ,null=True)
    bproduct = models.ForeignKey('Details',null=True,on_delete=models.CASCADE)
    b_amount = models.FloatField(max_length = 20, default = '', null = False)
    def __str__(self):
        return self.m_user.m_name+" "+self.b_id.b_name  



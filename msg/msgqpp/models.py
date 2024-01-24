from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=100)
    
class Product(models.Model):
    name=models.CharField(max_length=20,verbose_name='Product Name')
    #price=models.FloatField()
    pdetails=models.CharField(max_length=50)
    cate=models.IntegerField(verbose_name='Category')
    is_active=models.BooleanField(default=True,verbose_name='Avalable')

    def __str__(self):
        return self.name
class Product1(models.Model):
    name=models.CharField(max_length=20)
    #price=models.FloatField()
    pdetails=models.CharField(max_length=50)
    cate=models.IntegerField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Product2(models.Model):
    CAT=((1,'Mobile'),(2,'Cloth'),(3,'Cloth'))
    name=models.CharField(max_length=20,verbose_name='Product Name')
    price=models.FloatField()
    pdetails=models.CharField(max_length=50)
    cate=models.IntegerField(verbose_name='Category',choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name='Avalable')
    pimage=models.ImageField(upload_to='image')
    def __str__(self):
        return self.name
    

def __str__(self):
    return self.name1

class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product2,on_delete=models.CASCADE,db_column="pid")
    gty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Product2,on_delete=models.CASCADE,db_column="pid")
    gty=models.IntegerField(default=1)
    

    



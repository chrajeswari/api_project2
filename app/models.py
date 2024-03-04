from django.db import models

# Create your models here.

class Productcatogery(models.Model):
    product_catogery_id=models.IntegerField(primary_key=True)
    product_catogery_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_catogery_name
    
class Product(models.Model):
    product_catogery_id=models.ForeignKey(Productcatogery,on_delete=models.CASCADE)
    product_id=models.IntegerField()
    Product_name=models.CharField(max_length=100)
    Product_brand=models.CharField(max_length=100)
    Product_price=models.IntegerField()
    
from django.db import models

class user_info(models.Model):
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    quantity = models.IntegerField(default='0')
    price = models.IntegerField(default= '0.0')
    image = models.ImageField(upload_to='users/%Y/%m/%d/', default='img/feasta.jpeg')
    description = models.CharField(max_length=500)

    
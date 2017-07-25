from django.db import models

# Create your models here.

class Product(models.Model):
    p_title = models.CharField(max_length=100)
    p_desc = models.TextField()
    p_price = models.SmallIntegerField()
    p_image = models.URLField(max_lenth=200)


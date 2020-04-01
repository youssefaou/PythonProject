from django.db import models

class products(models.Model):
    product_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=10)

    def __str__(self):
        return  self.product_name

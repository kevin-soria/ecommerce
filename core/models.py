from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max(max_length=100))
    

class OrderItem(models.Model):
    pass


class Order(model.Model):
    pass

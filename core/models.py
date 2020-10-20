from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
     
    def __str__(self):
        return self.title
    

class OrderItem(models.Model):
    def __str__(self):
        return self.title
    pass


class Order(model.Model):
    def __str__(self):
        return self.title
    pass

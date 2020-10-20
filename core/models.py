from django.conf import settings
from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
     
    def __str__(self):
        return self.title
    

class OrderItem(models.Model):
    def __str__(self):
        return self.title


class Order(model.Model):
    user = mdels.models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
         return self.user.username
    

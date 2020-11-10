from django.shortcuts import render  j 
from .models import Item

# Create your views here.
def item_list(request):
    return render(request, "item_list.html", context=)
from sre_parse import CATEGORIES
from django.shortcuts import render
from . models import Product

# Create your views here.
def trending(request):
    items = Product.objects.all()
    categories = sorted({item.category for item in items})
    return render(request, 'trending.html', context={'items': items,'categories': categories}) 
"https://github.com/dipta406/django.git"   
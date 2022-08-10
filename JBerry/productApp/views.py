from itertools import product
from sre_parse import CATEGORIES
from django.shortcuts import render
from . models import Product

# Create your views here.
def trending(request):
    items = Product.objects.all()
    categories = sorted({item.category for item in items})
    return render(request, 'trending.html', context={'items': items,'categories': categories, 'CartCount': request.session['CartCount']}) 
def filterByCat(request,category):
   filtered_items = Product.objects.filter(category=category)
   return render(request, 'trending.html', context={'items': filtered_items ,'categories': category,'CartCount': request.session['CartCount']})

def product_details(request,pid):
    item = Product.objects.get(pid = pid)
    return render(request, 'product-details.html', context={'item': item})
def search(request):
    keywords = request.POST['keywords'].split(' ')
    items = Product.objects.filter(title__icontains =keywords[0])
    items = Product.objects.filter(pid__icontains =keywords[0])
    items= items.union(Product.objects.filter(desc__icontains =keywords[0]))
    for keyword in keywords[1:]:
        items= items.union(Product.objects.filter(desc__icontains =keywords[0]))
        items = items.union(Product.objects.filter(title__icontains =keywords[0]))
        items = items.union(Product.objects.filter(pid__icontains =keywords[0]))
    categories ={item.category for item in items} 
    return render(request,'search.html', context ={'items':items,'categories': categories})
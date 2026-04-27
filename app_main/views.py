from django.shortcuts import render

from .models import Product

def products(request):
    product = Product.objects.all()

    return render(request,"products.html", {"product":product})

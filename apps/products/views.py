from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    total_products_count = products.count()
    return render(request, "products/list.html", {"products": products, "total_products_count": total_products_count})

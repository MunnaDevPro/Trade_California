from django.shortcuts import render
from apps.products.models import Product, Category
from apps.services.models import ServiceType
from apps.core.models import Mentor, CompanyValue

def home(request):
    featured_products = Product.objects.filter(is_featured=True)[:4]
    services = ServiceType.objects.all()[:3]
    return render(request, "core/home.html", {"featured_products": featured_products, "services": services})

def about(request):
    mentors = Mentor.objects.filter(is_active=True).order_by('order')
    values = CompanyValue.objects.filter(is_active=True).order_by('order')
    return render(request, "core/about.html", {
        "mentors": mentors,
        "values": values
    })

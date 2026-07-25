from django.shortcuts import render
from django.core.paginator import Paginator
from apps.products.models import Product, Category
from apps.services.models import ServiceType
from apps.core.models import Mentor, CompanyValue

def home(request):
    featured_products_list = Product.objects.all().order_by('-id')
    paginator = Paginator(featured_products_list, 8)
    page_number = request.GET.get('page')
    featured_products = paginator.get_page(page_number)
    
    services = ServiceType.objects.all()[:3]
    return render(request, "core/home.html", {"featured_products": featured_products, "services": services})

def about(request):
    mentors = Mentor.objects.filter(is_active=True).order_by('order')
    values = CompanyValue.objects.filter(is_active=True).order_by('order')
    return render(request, "core/about.html", {
        "mentors": mentors,
        "values": values
    })

from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import NewsletterSubscriber

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thank you for subscribing to our newsletter!")
            else:
                messages.info(request, "You are already subscribed to our newsletter.")
    
    # Redirect to the previous page or home if HTTP_REFERER is not available
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

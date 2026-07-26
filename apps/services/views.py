from django.shortcuts import render
from .models import ServiceType, FAQ

def services_list(request):
    services = ServiceType.objects.all()
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, "services/list.html", {
        "services": services,
        "faqs": faqs,
    })

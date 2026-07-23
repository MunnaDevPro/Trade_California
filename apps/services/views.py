from django.shortcuts import render
from .models import ServiceType

def services_list(request):
    services = ServiceType.objects.all()
    return render(request, "services/list.html", {"services": services})

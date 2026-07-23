from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OfficeLocation
from .forms import ContactForm

def contact(request):
    locations = OfficeLocation.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        # Check if product is passed in query params
        initial = {}
        if 'product' in request.GET:
            initial['message'] = f"I am interested in {request.GET['product']}. Please send more information."
        form = ContactForm(initial=initial)

    return render(request, "contact/contact.html", {"locations": locations, "form": form})

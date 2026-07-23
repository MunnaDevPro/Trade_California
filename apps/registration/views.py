from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration request has been submitted successfully!')
            return redirect('registration')
    else:
        # Check if role is passed in query params
        initial = {}
        if 'role' in request.GET:
            initial['role'] = request.GET['role']
        form = RegistrationForm(initial=initial)

    return render(request, "registration/form.html", {'form': form})

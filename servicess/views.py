from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Service, Booking
from .forms import BookingForm


def service_view(request):
    services = Service.objects.all()  # Fetch all services from the database
    # Create a dictionary to store services grouped by title
    services_by_title = {}

    for service in services:
        title = service.title
        if title not in services_by_title:
            services_by_title[title] = []
        services_by_title[title].append(service)

    return render(request, 'servicess/services.html', {'services_by_title': services_by_title})


def book_service(request, service_id):
    service = Service.objects.get(id=service_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.service = service
            booking.save()
            return render(request, 'servicess/booking_confirmation.html')  # Redirect to the services page or a confirmation page
    else:
        form = BookingForm()

    return render(request, 'servicess/book_service.html', {'form': form, 'service': service})


def service_search(request):
    search_query = request.GET.get('search_query', '')
    location_filter = request.GET.get('location', '')
    category_filter = request.GET.get('category', '')
    features_filter = request.GET.get('features', '')

    # Use Q objects to perform an OR search across multiple fields
    services = Service.objects.filter(
        Q(title__icontains=search_query) |
        Q(sub_title__icontains=search_query)
    )

    return render(request, 'servicess/search_results.html', {'services': services, 'search_query': search_query})

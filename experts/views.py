from django.contrib.auth import logout
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import WorkCategory, WorkSubcategory, ServiceProvider
from .forms import ServiceProviderForm
#from ..servicess.models import Booking


#from ..servicess.models import Booking





def register_service_provider(request):
    categories = WorkCategory.objects.all()
    if request.method == "POST":
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    else:
        form = ServiceProviderForm()

    return render(request, 'experts/service_provider_registration.html', {'form': form, 'categories': categories})


def get_subcategories(request):
    if request.is_ajax() and request.method == "GET":
        category_id = request.GET.get("category_id")
        subcategories = WorkSubcategory.objects.filter(category_id=category_id).values("id", "name")
        return JsonResponse(list(subcategories), safe=False)
    return JsonResponse({}, status=400)


def logout_view(request):
    logout(request)
    return redirect('homepage')  # Redirect to your desired page after logout


def login_page(request):
    context = {'message': 'Invalid Credentials......'}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = ServiceProvider.objects.filter(Q(email=email), Q(password=password))
        if data:
            return redirect('services')
        else:
            return renderpyth(request, 'experts/expert_login_page.html', context)
    return render(request, 'experts/expert_login_page.html')


def my_bookings(request):
     expert = ServiceProvider.objects.get(user=request.user)

     bookings = Booking.objects.filter(
         service__title=expert.work_category.name,
         service__sub_title=expert.work_subcategory.name,
         city=expert.city,
     )

     return render(request, 'experts/my_bookings.html', {'bookings': bookings})

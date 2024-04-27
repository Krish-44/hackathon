from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'core/index.html')


def about_us(request):
    return render(request, 'core/about.html')
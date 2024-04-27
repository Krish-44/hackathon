from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('servicess/', views.service_view, name='services'),
    path('servicess/<int:service_id>/book/', views.book_service, name='book_service'),
    path('service-search/', views.service_search, name='service_search'),
]

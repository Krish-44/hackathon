from django.urls import path
from . import views

urlpatterns = [
    path('expert-login/', views.login_page, name='expert_login'),
    path('expert-register/',views.register_service_provider,name='expert_register'),
    path('expert-logout/', views.logout_view, name='expert_logout'),
    path("get_subcategories/", views.get_subcategories, name="get_subcategories"),
    path('expert-bookings/', views.my_bookings, name='expert_bookings')
]

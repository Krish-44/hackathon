from django.contrib import admin
from .models import Service, Booking


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'description', 'price', 'image_url', 'alt_text')
    list_display_links = ('title',)


# Register the Service model with the custom admin class
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking)
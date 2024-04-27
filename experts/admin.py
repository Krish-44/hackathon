from django.contrib import admin
from .models import ServiceProvider, WorkCategory, WorkSubcategory


class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'city', 'work_category', 'work_subcategory')
    search_fields = ('name', 'email', 'city', 'work_category__name', 'work_subcategory__name')
    list_filter = ('work_category', 'work_subcategory')


class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class WorkSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


admin.site.register(ServiceProvider, ServiceProviderAdmin)
admin.site.register(WorkCategory, WorkCategoryAdmin)
admin.site.register(WorkSubcategory, WorkSubcategoryAdmin)

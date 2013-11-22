from django.contrib import admin
from .models import Service, ServiceType


class ServiceAdmin(admin.ModelAdmin):

    filter_horizontal = ("service_type", )
    list_display = ("name", "pre_requirements")


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "description")


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
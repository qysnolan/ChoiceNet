from django.contrib import admin
from .models import Service, ServiceType


class ServiceAdmin(admin.ModelAdmin):

    list_display = ("name", "service_id", "owner", "service_cost",
                    "service_type", "service_bandwidth", "service_latency",
                    "date_created", "date_modified", "date_used")
    search_fields = ("name", "description", "owner", )


class ServiceTypeAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "description")
    search_fields = ("name", "category", "description")


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
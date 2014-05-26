from django.contrib import admin
from .models import Service, ServiceType, ServiceOwner


class ServiceAdmin(admin.ModelAdmin):

    list_display = ("name", "service_id", "owner", "service_cost",
                    "service_type", "service_bandwidth", "service_latency",
                    "date_created", "date_modified", "date_used")
    search_fields = ("name", "description", "owner", )


class ServiceTypeAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "description")
    search_fields = ("name", "category", "description")


class ServiceOwnerAdmin(admin.ModelAdmin):
    list_display = ("owner", "service", "share_cost")
    search_fields = ("owner", "service")


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(ServiceOwner, ServiceOwnerAdmin)
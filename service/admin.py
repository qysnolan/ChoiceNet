from django.contrib import admin
from .models import Service, ServiceType


class ServiceAdmin(admin.ModelAdmin):

    filter_horizontal = ("service_type", )
    list_display = ("name", "process_id", "service_output", "service_input",
                    "pre_requirements", "cost", "date_created", )
    search_fields = ("name", "service_output", "service_input",
                     "pre_requirements")


class ServiceTypeAdmin(admin.ModelAdmin):

    list_display = ("name", "category", "description")
    search_fields = ("name", "category", "description")


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceType, ServiceTypeAdmin)
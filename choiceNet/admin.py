from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ("date_created", "buyer", "service", "number",
                    "amount", "is_paid", "is_active", )
    list_filter = ("is_paid", "is_active", )
    search_fields = ("date_created", "buyer", "service", )


admin.site.register(Invoice, InvoiceAdmin)

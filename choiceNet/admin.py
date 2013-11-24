from django.contrib import admin
from .models import Invoice


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ("date_created", "buyer", "service", "number",
                    "amount", "paid", )
    list_filter = ("paid", )
    search_fields = ("date_created", "buyer", "service", )


admin.site.register(Invoice, InvoiceAdmin)

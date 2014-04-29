from django.contrib import admin
from .models import *


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ("date_created", "buyer", "service", "number",
                    "amount", "is_paid", "is_active", )
    list_filter = ("is_paid", "is_active", )
    search_fields = ("date_created", "buyer", "service", )


class BalanceAdmin(admin.ModelAdmin):

    list_display = ("user", "balance", )
    search_fields = ("user", )


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Balance, BalanceAdmin)

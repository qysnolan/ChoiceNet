from django.contrib import admin
from .models import *


class InvoiceAdmin(admin.ModelAdmin):

    list_display = ("date_created", "buyer", "service", "number",
                    "amount", "is_paid", "is_active", )
    list_filter = ("is_paid", "is_active", )
    search_fields = ("date_created", "buyer", "service", )


class CommentAdmin(admin.ModelAdmin):

    list_display = ("user", "service", "created_date", "rate", "is_provider")
    list_filter = ("is_provider", )
    search_fields = ("user", "service")


class BalanceAdmin(admin.ModelAdmin):

    list_display = ("user", "balance", )
    search_fields = ("user", )


class IncomeAdmin(admin.ModelAdmin):

    list_display = ("provider", "income", "updated_time")
    search_fields = ("provider", )


class SessionAdmin(admin.ModelAdmin):

    list_display = ("user", "session", "start_time", "end_time", "is_login")
    search_fields = ("user", )


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Balance, BalanceAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Session, SessionAdmin)

from django.contrib import admin
from .models import *
from .forms import TransactionAdminForm

class TransactionAdmin(admin.ModelAdmin):
    form = TransactionAdminForm
    list_display = (
        "created_at",
        "status",
        "type",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    list_filter = (
        "status",
        "type",
        "category",
        "subcategory",
        "created_at",
    )

    class Media:
        js = ("admin/js/transaction_admin.js",)

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Transaction, TransactionAdmin)
# admin.site.register(Transaction)

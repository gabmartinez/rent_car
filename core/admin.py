from django.contrib import admin

from core.forms import CustomerForm, EmployeeForm
from core.mixins import ExportAdminMixin
from core.models import Customer, Employee


@admin.register(Customer)
class CustomerAdmin(ExportAdminMixin, admin.ModelAdmin):
    form = CustomerForm
    list_display = (
        "name",
        "person_type",
        "document_number",
        "credit_limit",
        "total_credit_used",
        "is_active",
    )
    search_fields = ("name", "document_number")
    list_filter = ("is_active", "person_type")


@admin.register(Employee)
class EmployeeAdmin(ExportAdminMixin, admin.ModelAdmin):
    form = EmployeeForm
    list_display = (
        "name",
        "document_number",
        "work_shift",
        "commission_percentage",
        "entry_date",
        "is_active",
    )
    search_fields = ("name", "document_number")
    list_filter = ("is_active", "work_shift")

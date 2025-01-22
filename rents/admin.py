from django.contrib import admin
from django.db import transaction
from django.db.models import Sum

from core.mixins import ExportAdminMixin
from rents.forms import RentForm, InspectionForm
from rents.models import Inspection, Rent

from django.utils.translation import gettext_lazy as _


@admin.register(Inspection)
class InspectionAdmin(ExportAdminMixin, admin.ModelAdmin):
    form = InspectionForm
    list_display = (
        "rent",
        "has_scratches",
        "fuel_quantity",
        "has_spare_tire",
        "has_broken_glass",
        "has_jack",
        "front_left_tire_condition",
        "front_right_tire_condition",
        "rear_left_tire_condition",
        "rear_right_tire_condition",
        "inspection_employee",
        "inspection_date",
        "is_active",
    )
    search_fields = (
        "rent__vehicle__description",
        "rent__customer__name",
        "inspection_employee__name",
    )
    list_filter = (
        "is_active",
        "has_scratches",
        "fuel_quantity",
        "has_spare_tire",
        "has_broken_glass",
        "has_jack",
        "front_left_tire_condition",
        "front_right_tire_condition",
        "rear_left_tire_condition",
        "rear_right_tire_condition",
    )
    autocomplete_fields = ("rent", "inspection_employee")


class InspectionInline(admin.StackedInline):
    model = Inspection
    extra = 0
    form = InspectionForm
    autocomplete_fields = ("inspection_employee",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "fuel_quantity",
                    "is_active",
                )
            },
        ),
        (
            _("Vehicle Conditions"),
            {
                "fields": (
                    "has_scratches",
                    "has_broken_glass",
                )
            },
        ),
        (
            _("Equipment Conditions"),
            {
                "fields": (
                    "has_spare_tire",
                    "has_jack",
                )
            },
        ),
        (
            _("Tire Conditions"),
            {
                "fields": (
                    "front_left_tire_condition",
                    "front_right_tire_condition",
                    "rear_left_tire_condition",
                    "rear_right_tire_condition",
                )
            },
        ),
        (
            _("Inspection Information"),
            {"fields": ("inspection_employee", "inspection_date")},
        ),
    )


@admin.register(Rent)
class RentAdmin(ExportAdminMixin, admin.ModelAdmin):
    form = RentForm
    list_display = ("employee", "vehicle", "customer", "rent_date")
    search_fields = ("employee__name", "vehicle__description", "customer__name")
    list_filter = ("rent_date",)
    autocomplete_fields = ("employee", "vehicle", "customer")

    def get_inlines(self, request, obj):
        if obj:
            return [InspectionInline]
        return []

    def _update_total_credit_used_for_customer(self, customer):
        total_credit_used = (
            Rent.objects.filter(customer=customer, is_active=True)
            .aggregate(total_credit_used=Sum("total_price"))
            .get("total_credit_used")
        )
        customer.total_credit_used = total_credit_used or 0
        customer.save(update_fields=["total_credit_used"])

    def save_model(self, request, obj, form, change):
        obj.total_days = (obj.return_date - obj.rent_date).days
        obj.total_price = obj.total_days * obj.price_per_day
        super().save_model(request, obj, form, change)

        transaction.on_commit(
            lambda: self._update_total_credit_used_for_customer(obj.customer)
        )

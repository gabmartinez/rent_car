from django.contrib import admin

from core.mixins import ExportAdminMixin
from vehicles.models import VehicleType, VehicleBrand, VehicleModel, FuelType, Vehicle


@admin.register(VehicleType)
class VehicleTypeAdmin(ExportAdminMixin, admin.ModelAdmin):
    list_display = ("description", "is_active")
    search_fields = ("description",)
    list_filter = ("is_active",)


@admin.register(VehicleBrand)
class VehicleBrandAdmin(ExportAdminMixin, admin.ModelAdmin):
    list_display = ("description", "is_active")
    search_fields = ("description",)
    list_filter = ("is_active",)


@admin.register(VehicleModel)
class VehicleModelAdmin(ExportAdminMixin, admin.ModelAdmin):
    list_display = ("description", "is_active", "brand")
    search_fields = ("description",)
    list_filter = ("is_active",)


@admin.register(FuelType)
class FuelTypeAdmin(ExportAdminMixin, admin.ModelAdmin):
    list_display = ("description", "is_active")
    search_fields = ("description",)
    list_filter = ("is_active",)


@admin.register(Vehicle)
class VehicleAdmin(ExportAdminMixin, admin.ModelAdmin):
    list_display = (
        "description",
        "chassis_number",
        "motor_number",
        "plate_number",
        "vehicle_type",
        "brand",
        "vehicle_model",
        "fuel_type",
        "is_active",
    )
    search_fields = ("description", "chassis_number", "motor_number", "plate_number")
    list_filter = ("is_active", "vehicle_type", "brand", "vehicle_model", "fuel_type")
    autocomplete_fields = ("brand", "vehicle_type", "vehicle_model", "fuel_type")

from django.db import models
from django.utils.translation import gettext as _


class VehicleType(models.Model):
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Vehicle Type")
        verbose_name_plural = _("Vehicle Types")

    def __str__(self):
        return self.description


class VehicleBrand(models.Model):
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.description


class VehicleModel(models.Model):
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    brand = models.ForeignKey(
        VehicleBrand,
        on_delete=models.CASCADE,
        related_name="models",
        verbose_name=_("Brand"),
    )

    class Meta:
        verbose_name = _("Vehicle Model")
        verbose_name_plural = _("Vehicle Models")

    def __str__(self):
        return self.description


class FuelType(models.Model):
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Fuel Type")
        verbose_name_plural = _("Fuel Types")

    def __str__(self):
        return self.description


class Vehicle(models.Model):
    description = models.CharField(max_length=100, verbose_name=_("Description"))
    chassis_number = models.CharField(max_length=100, verbose_name=_("Chassis Number"))
    motor_number = models.CharField(max_length=100, verbose_name=_("Motor Number"))
    plate_number = models.CharField(max_length=100, verbose_name=_("Plate Number"))
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE,
        related_name="vehicles",
        verbose_name=_("Vehicle Type"),
    )
    brand = models.ForeignKey(
        VehicleBrand,
        on_delete=models.CASCADE,
        related_name="vehicles",
        verbose_name=_("Brand"),
    )
    vehicle_model = models.ForeignKey(
        VehicleModel,
        on_delete=models.CASCADE,
        related_name="vehicles",
        verbose_name=_("Model"),
    )
    fuel_type = models.ForeignKey(
        FuelType,
        on_delete=models.CASCADE,
        related_name="vehicles",
        verbose_name=_("Fuel Type"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Vehicle")
        verbose_name_plural = _("Vehicles")

    def __str__(self):
        return f"{self.description} - {self.plate_number}"

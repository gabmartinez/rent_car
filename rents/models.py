from django.db import models
from django.utils.translation import gettext as _


class FuelQuantity(models.TextChoices):
    QUARTER = "QUARTER", _("1/4")
    HALF = "HALF", _("1/2")
    THREE_QUARTERS = "THREE_QUARTERS", _("3/4")
    FULL = "FULL", _("Full")


class Rent(models.Model):
    employee = models.ForeignKey(
        "core.Employee",
        on_delete=models.CASCADE,
        related_name="rents",
        verbose_name=_("Employee"),
    )
    customer = models.ForeignKey(
        "core.Customer",
        on_delete=models.CASCADE,
        related_name="rents",
        verbose_name=_("Customer"),
    )
    vehicle = models.ForeignKey(
        "vehicles.Vehicle",
        on_delete=models.CASCADE,
        related_name="rents",
        verbose_name=_("Vehicle"),
    )
    rent_date = models.DateField(verbose_name=_("Rent Date"))
    return_date = models.DateField(verbose_name=_("Return Date"))
    total_days = models.PositiveSmallIntegerField(
        verbose_name=_("Total Days"), default=0, editable=False
    )
    price_per_day = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price Per Day")
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Price"), editable=False
    )
    comment = models.TextField(verbose_name=_("Comment"), blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Rent")
        verbose_name_plural = _("Rents")

    def __str__(self):
        return f"{self.customer} - {self.vehicle}"


class TireCondition(models.TextChoices):
    VERY_BAD = "VERY_BAD", _("Very Bad")
    BAD = "BAD", _("Bad")
    REGULAR = "REGULAR", _("Regular")
    GOOD = "GOOD", _("Good")
    VERY_GOOD = "VERY_GOOD", _("Very Good")


class InspectionType(models.TextChoices):
    PRE_RENT = "PRE_RENT", _("Pre Rent")
    POST_RENT = "POST_RENT", _("Post Rent")


class Inspection(models.Model):
    inspection_type = models.CharField(
        max_length=15,
        choices=InspectionType.choices,
        default=InspectionType.PRE_RENT,
        verbose_name=_("Inspection Type"),
    )
    rent = models.ForeignKey(
        Rent,
        on_delete=models.CASCADE,
        related_name="inspections",
        verbose_name=_("Rent"),
    )
    has_scratches = models.BooleanField(verbose_name=_("Has Scratches"))
    fuel_quantity = models.CharField(
        max_length=15,
        choices=FuelQuantity.choices,
        default=FuelQuantity.FULL,
        verbose_name=_("Fuel Quantity"),
    )
    has_spare_tire = models.BooleanField(verbose_name=_("Has Spare Tire"))
    has_broken_glass = models.BooleanField(verbose_name=_("Has Broken Glass"))
    has_jack = models.BooleanField(verbose_name=_("Has Jack"))
    front_left_tire_condition = models.CharField(
        max_length=15,
        choices=TireCondition.choices,
        default=TireCondition.GOOD,
        verbose_name=_("Front Left Tire Condition"),
    )
    front_right_tire_condition = models.CharField(
        max_length=15,
        choices=TireCondition.choices,
        default=TireCondition.GOOD,
        verbose_name=_("Front Right Tire Condition"),
    )
    rear_left_tire_condition = models.CharField(
        max_length=15,
        choices=TireCondition.choices,
        default=TireCondition.GOOD,
        verbose_name=_("Rear Left Tire Condition"),
    )
    rear_right_tire_condition = models.CharField(
        max_length=15,
        choices=TireCondition.choices,
        default=TireCondition.GOOD,
        verbose_name=_("Rear Right Tire Condition"),
    )
    inspection_employee = models.ForeignKey(
        "core.Employee",
        on_delete=models.CASCADE,
        related_name="inspections",
        verbose_name=_("Inspection Employee"),
    )
    inspection_date = models.DateField(verbose_name=_("Inspection Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    comment = models.TextField(verbose_name=_("Comment"), blank=True, null=True)

    class Meta:
        verbose_name = _("Inspection")
        verbose_name_plural = _("Inspections")

    def __str__(self):
        return f"{self.rent}"

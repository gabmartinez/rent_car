from django.db import models
from django.utils.translation import gettext as _


class PersonType(models.TextChoices):
    JURIDICAL = "JURIDICAL", _("Juridical")
    PHYSICAL = "PHYSICAL", _("Physical")


class Customer(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    document_number = models.CharField(
        max_length=20, unique=True, verbose_name=_("Document Number")
    )
    credit_card_number = models.CharField(
        max_length=20, verbose_name=_("Credit Card Number"), blank=True, null=True
    )
    credit_limit = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Credit Limit"), default=0
    )
    total_credit_used = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Total Credit Used"), default=0
    )
    person_type = models.CharField(
        max_length=10,
        choices=PersonType.choices,
        default=PersonType.PHYSICAL,
        verbose_name=_("Person Type"),
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.name} - {self.document_number}"


class WorkShift(models.TextChoices):
    MORNING = "MORNING", _("Morning")
    AFTERNOON = "AFTERNOON", _("Afternoon")
    NIGHT = "NIGHT", _("Night")


class Employee(models.Model):
    name = models.CharField(max_length=150, verbose_name=_("Name"))
    document_number = models.CharField(
        max_length=20, unique=True, verbose_name=_("Document Number")
    )
    work_shift = models.CharField(
        max_length=10,
        choices=WorkShift.choices,
        default=WorkShift.MORNING,
        verbose_name=_("Work Shift"),
    )
    commission_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name=_("Commission Percentage")
    )
    entry_date = models.DateField(verbose_name=_("Entry Date"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees")

    def __str__(self):
        return f"{self.name} - {self.document_number}"

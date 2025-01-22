from django import forms
from django.db.models import Sum

from rents import models
from django.utils.translation import gettext as _


class RentForm(forms.ModelForm):
    class Meta:
        model = models.Rent
        fields = "__all__"

    def clean_rent_date(self):
        """Check if the rent date is less than today."""
        rent_date = self.cleaned_data["rent_date"]
        if rent_date < rent_date.today():
            raise forms.ValidationError(_("The rent date cannot be less than today."))
        return rent_date

    def clean_return_date(self):
        """Check if the return date is less or equal than today."""
        return_date = self.cleaned_data["return_date"]
        if return_date <= return_date.today():
            raise forms.ValidationError(
                _("The return date cannot be less or equal than today.")
            )
        return return_date

    def clean_price_per_day(self):
        """Check if the price per day is greater than zero."""
        price_per_day = self.cleaned_data["price_per_day"]
        if price_per_day <= 0:
            raise forms.ValidationError(
                _("The price per day must be greater than zero.")
            )
        return price_per_day

    def clean_customer(self):
        """Check if the customer is active."""
        customer = self.cleaned_data.get("customer")
        if not customer or not customer.is_active:
            raise forms.ValidationError(_("The customer is not active."))
        return customer

    def clean_vehicle(self):
        """Check if the vehicle is active."""
        vehicle = self.cleaned_data.get("vehicle")
        if not vehicle or not vehicle.is_active:
            raise forms.ValidationError(_("The vehicle is not active."))
        return vehicle

    def clean(self):
        """Check if the total days is greater than zero and if the selected vehicle is available."""
        cleaned_data = super().clean()
        rent_date = cleaned_data.get("rent_date")
        return_date = cleaned_data.get("return_date")

        if not rent_date or not return_date:
            raise forms.ValidationError(
                _("The rent date and return date are required.")
            )

        if rent_date > return_date or rent_date == return_date:
            raise forms.ValidationError(
                _("The rent date must be less than the return date.")
            )

        total_days = (return_date - rent_date).days

        if total_days <= 0:
            raise forms.ValidationError(_("The total days must be greater than zero."))

        price_per_day = cleaned_data.get("price_per_day")
        if price_per_day is None:
            raise forms.ValidationError(_("The price per day is required."))

        vehicle = cleaned_data.get("vehicle")
        rent_qs = vehicle.rents.filter(is_active=True).exclude(pk=self.instance.pk)
        for rent in rent_qs:
            if (
                rent.rent_date <= rent_date <= rent.return_date
                or rent.rent_date <= return_date <= rent.return_date
            ):
                raise forms.ValidationError(
                    _("The vehicle is already rented in the selected period.")
                )

        total_credit_used = (
            rent_qs.filter(customer=cleaned_data["customer"])
            .aggregate(total_credit_used=Sum("total_price"))
            .get("total_credit_used")
        )
        credit_available = cleaned_data["customer"].credit_limit - (
            total_credit_used or 0
        )

        if (total_days * price_per_day) > credit_available:
            raise forms.ValidationError(
                _("The customer does not have enough credit available.")
            )
        return cleaned_data


class InspectionForm(forms.ModelForm):
    class Meta:
        model = models.Inspection
        fields = "__all__"

    def clean_rent(self):
        """Check if the rent is active."""
        rent = self.cleaned_data.get("rent")
        if not rent or not rent.is_active:
            raise forms.ValidationError(_("The rent is not active."))
        return rent

    def clean_inspection_date(self):
        """Check if the inspection date is less than today."""
        inspection_date = self.cleaned_data["inspection_date"]
        if inspection_date > inspection_date.today():
            raise forms.ValidationError(
                _("The inspection date cannot be greater than today.")
            )
        return inspection_date

    def clean(self):
        cleaned_data = super().clean()
        inspection_date = cleaned_data["inspection_date"]
        rent = cleaned_data["rent"]
        if inspection_date < rent.rent_date or inspection_date > rent.return_date:
            raise forms.ValidationError(
                _(
                    "The inspection date must be between the rent date and the return date."
                )
            )
        return cleaned_data

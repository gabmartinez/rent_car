from django import forms

from core.utils import (
    physical_document_number_validator,
    juridical_document_number_validator,
    credit_card_number_validator,
)
from core import models
from django.utils.translation import gettext as _

from core.models import PersonType


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"

    def clean_credit_limit(self):
        """Check if the credit limit is zero or greater."""
        credit_limit = self.cleaned_data["credit_limit"]
        if credit_limit < 0:
            raise forms.ValidationError(_("The credit limit must be zero or greater."))
        return credit_limit

    def clean_credit_card_number(self):
        """Check if the credit card number is valid."""
        credit_card_number = self.cleaned_data["credit_card_number"]
        if credit_card_number is None:
            return credit_card_number

        if not credit_card_number_validator(credit_card_number):
            raise forms.ValidationError(_("The credit card number is invalid."))
        return credit_card_number

    def clean(self):
        cleaned_data = super().clean()
        person_type = cleaned_data["person_type"]
        document_number = cleaned_data["document_number"]
        if (
            person_type == PersonType.PHYSICAL
            and not physical_document_number_validator(document_number)
        ):
            raise forms.ValidationError(_("The document number is invalid."))
        elif (
            person_type == PersonType.JURIDICAL
            and not juridical_document_number_validator(document_number)
        ):
            raise forms.ValidationError(_("The document number is invalid."))
        return cleaned_data


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.Employee
        fields = "__all__"

    def clean_document_number(self):
        """Check if the document number is valid."""
        document_number = self.cleaned_data["document_number"]
        if not physical_document_number_validator(document_number):
            raise forms.ValidationError(_("The document number is invalid."))
        return document_number

    def clean_commission_percentage(self):
        """Check if the commission percentage is zero or greater."""
        commission_percentage = self.cleaned_data["commission_percentage"]
        if commission_percentage < 0:
            raise forms.ValidationError(
                _("The commission percentage must be zero or greater.")
            )
        return commission_percentage

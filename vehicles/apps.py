from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class VehiclesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vehicles"
    verbose_name = _("Vehicles")

# Generated by Django 5.1.4 on 2025-01-21 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FuelType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Estado")),
            ],
            options={
                "verbose_name": "Tipo Combustible",
                "verbose_name_plural": "Tipos de Combustible",
            },
        ),
        migrations.CreateModel(
            name="VehicleBrand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Estado")),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.CreateModel(
            name="VehicleType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Estado")),
            ],
            options={
                "verbose_name": "Tipo de Vehículo",
                "verbose_name_plural": "Tipos de Vehículos",
            },
        ),
        migrations.CreateModel(
            name="VehicleModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="models",
                        to="vehicles.vehiclebrand",
                        verbose_name="Marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "Modelo",
                "verbose_name_plural": "Modelos",
            },
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="Descripción"),
                ),
                (
                    "chassis_number",
                    models.CharField(max_length=100, verbose_name="No. Chasis"),
                ),
                (
                    "motor_number",
                    models.CharField(max_length=100, verbose_name="No. Motor"),
                ),
                (
                    "plate_number",
                    models.CharField(max_length=100, verbose_name="No. Placa"),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "fuel_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="vehicles.fueltype",
                        verbose_name="Tipo Combustible",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="vehicles.vehiclebrand",
                        verbose_name="Marca",
                    ),
                ),
                (
                    "vehicle_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="vehicles.vehiclemodel",
                        verbose_name="Modelo",
                    ),
                ),
                (
                    "vehicle_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vehicles",
                        to="vehicles.vehicletype",
                        verbose_name="Tipo de Vehículo",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vehículo",
                "verbose_name_plural": "Vehículos",
            },
        ),
    ]

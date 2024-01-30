# Generated by Django 5.0.1 on 2024-01-30 11:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("billboards", "0008_billboard_price_alter_billboard_is_verified"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Booking",
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
                    "period",
                    models.CharField(
                        choices=[
                            ("weekly", "weekly"),
                            ("monthly", "monthly"),
                            ("annually", "annually"),
                        ],
                        max_length=8,
                    ),
                ),
                ("timeline", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "billboard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="billboards.billboard",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

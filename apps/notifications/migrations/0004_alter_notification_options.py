# Generated by Django 5.0.1 on 2024-01-26 22:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notifications", "0003_alter_notification_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={"ordering": ("-created_at",)},
        ),
    ]

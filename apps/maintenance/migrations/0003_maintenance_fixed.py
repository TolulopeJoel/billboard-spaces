# Generated by Django 5.0.1 on 2024-02-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("maintenance", "0002_alter_maintenance_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="maintenance",
            name="fixed",
            field=models.BooleanField(default=False),
        ),
    ]

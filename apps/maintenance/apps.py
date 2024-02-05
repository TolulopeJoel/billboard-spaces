from django.apps import AppConfig


class MaintenanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.maintenance"

    def ready(self) -> None:
        import apps.maintenance.signals

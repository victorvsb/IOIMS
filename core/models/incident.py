from django.db import models
from django.conf import settings
from .enums import IncidentStatus

class Incident(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    incident_type = models.CharField(max_length=50)

    status = models.CharField(
        max_length=20,
        choices=IncidentStatus.choices,
        default=IncidentStatus.OPEN,
    )

    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reported_incidents",
    )

    created_at = models.DateTimeField(auto_now_add=True)

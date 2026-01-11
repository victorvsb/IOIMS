from django.db import models

class IncidentStatus(models.TextChoices):
    OPEN = "OPEN", "Open"
    ASSIGNED = "ASSIGNED", "Assigned"
    RESOLVED = "RESOLVED", "Resolved"
    CLOSED = "CLOSED", "Closed"

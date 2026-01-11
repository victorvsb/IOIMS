from models.incident import Incident


class IncidentRepository:
    @staticmethod
    def create(**data) -> Incident:
        return Incident.objects.create(**data)

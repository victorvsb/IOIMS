from core.models.incident import Incident
from core.dto.incident_dto import IncidentDTO


class IncidentSelector:
    @staticmethod
    def get_incident_by_id(incident_id: int) -> IncidentDTO:
        incident = Incident.objects.get(id=incident_id)
        return IncidentDTO(from_model=incident)
    
    @staticmethod
    def get_all_incidents() -> list[Incident]:
        return [IncidentDTO(from_model=inc) for inc in Incident.objects.all()]

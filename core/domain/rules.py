from .exceptions import InvalidIncidentData

def validate_incident_creation(*, title: str):
    if not title or not title.strip():
        raise InvalidIncidentData("Incident must have a title")

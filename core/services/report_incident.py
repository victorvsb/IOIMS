from commands.report_incident import ReportIncidentCommand
from domain.rules import validate_incident_creation
from repositories.incident_repository import IncidentRepository

def report_incident(*, command: ReportIncidentCommand):
    validate_incident_creation(title=command.title)

    return IncidentRepository.create(
        title=command.title,
        description=command.description,
        incident_type=command.incident_type,
        reported_by_id=command.reported_by_id,
    )

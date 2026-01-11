from dataclasses import dataclass

@dataclass(frozen=True)
class ReportIncidentCommand:
    title: str
    description: str
    incident_type: str
    reported_by_id: int

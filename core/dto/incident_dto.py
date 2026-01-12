from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class IncidentDTO:
    """Data Transfer Object for Incident"""
    id: str
    title: str
    description: str
    incident_type: str
    status: str
    reported_by: str
    created_at: datetime
    
    def to_dict(self) -> dict:
        """Convert DTO to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'incident_type': self.incident_type,
            'status': self.status,
            'reported_by': self.reported_by,
            'created_at': self.created_at,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'IncidentDTO':
        """Create DTO from dictionary"""
        return cls(**data)
    
    @classmethod
    def from_model(cls, model) -> 'IncidentDTO':
        """Create DTO from model instance"""
        return cls(
            id=model.id,
            title=model.title,
            description=model.description,
            incident_type=model.incident_type,
            status=model.status,
            reported_by=model.reported_by,
            created_at=model.created_at,
        )

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class IncidentDTO:
    """Data Transfer Object for Incident"""
    id: str
    title: str
    description: str
    status: str
    severity: str
    created_at: datetime
    updated_at: datetime
    assigned_to: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    
    def to_dict(self) -> dict:
        """Convert DTO to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'severity': self.severity,
            'priority': self.priority,
            'assigned_to': self.assigned_to,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'due_date': self.due_date,
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
            status=model.status,
            severity=model.severity,
            created_at=model.created_at,
            updated_at=model.updated_at,
            assigned_to=model.assigned_to,
            priority=model.priority,
            due_date=model.due_date,
        )

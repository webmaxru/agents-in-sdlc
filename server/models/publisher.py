"""
Publisher model for the Tailspin Toys Crowd Funding platform.

This module defines the Publisher model representing game publishers
seeking crowdfunding for their titles.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Database model representing a game publisher.
    
    Attributes:
        id: Primary key identifier
        name: Name of the publisher
        description: Description of the publisher and their portfolio
        games: Relationship to all games published by this publisher
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate publisher name meets length requirements.
        
        Args:
            key: Field name being validated
            name: Publisher name to validate
            
        Returns:
            Validated name string
            
        Raises:
            ValueError: If name is too short
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """
        Validate publisher description meets length requirements.
        
        Args:
            key: Field name being validated
            description: Description to validate
            
        Returns:
            Validated description string or None
            
        Raises:
            ValueError: If description is too short
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self) -> str:
        """Return string representation of the Publisher instance."""
        return f'<Publisher {self.name}>'

    def to_dict(self) -> dict:
        """
        Convert Publisher instance to dictionary for JSON serialization.
        
        Returns:
            Dictionary containing publisher data and game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
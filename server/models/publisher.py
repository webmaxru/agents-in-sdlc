"""
Publisher model for the Tailspin Toys Crowd Funding platform.
This module defines the Publisher model representing game publishers
seeking funding for their titles.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Represents a game publisher on the crowdfunding platform.
    
    Attributes:
        id: Unique identifier for the publisher
        name: The name of the publisher
        description: Description of the publisher and their work
        games: Relationship to associated Game models
    """
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the publisher name meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            name: The publisher name to validate
            
        Returns:
            str: The validated name
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the publisher description meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            description: The description value to validate
            
        Returns:
            str: The validated description
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """
        Returns a string representation of the Publisher instance.
        
        Returns:
            str: String representation showing the publisher name
        """
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Converts the Publisher instance to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing publisher data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
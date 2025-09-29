"""
Publisher model for the Tailspin Toys Crowd Funding platform.
This module defines the Publisher data model representing game publishers,
including validation and serialization methods.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """
    Represents a game publisher on the crowdfunding platform.
    
    Attributes:
        id (int): Unique identifier for the publisher
        name (str): Publisher name (2-100 characters, must be unique)
        description (str): Publisher description (optional, minimum 10 characters when provided)
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
        Validate the publisher name field.
        
        Args:
            key (str): The field name being validated
            name (str): The name value to validate
            
        Returns:
            str: The validated name
            
        Raises:
            ValueError: If name is invalid (empty, wrong type, or too short)
        """
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """
        Validate the publisher description field.
        
        Args:
            key (str): The field name being validated
            description (str | None): The description value to validate
            
        Returns:
            str | None: The validated description
            
        Raises:
            ValueError: If description is invalid (wrong type or too short when provided)
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """
        Return a string representation of the Publisher instance.
        
        Returns:
            str: String representation showing publisher name
        """
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Convert the Publisher instance to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing publisher data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
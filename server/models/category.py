"""
Category model for the Tailspin Toys Crowd Funding platform.
This module defines the Category model representing game categories
used to organize games on the platform.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """
    Represents a game category on the crowdfunding platform.
    
    Attributes:
        id: Unique identifier for the category
        name: The name of the category
        description: Description of the category
        games: Relationship to associated Game models
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key, name):
        """
        Validates the category name meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            name: The category name to validate
            
        Returns:
            str: The validated name
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the category description meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            description: The description value to validate
            
        Returns:
            str: The validated description
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """
        Returns a string representation of the Category instance.
        
        Returns:
            str: String representation showing the category name
        """
        return f'<Category {self.name}>'
        
    def to_dict(self):
        """
        Converts the Category instance to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing category data including game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
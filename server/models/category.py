"""
Category model for the Tailspin Toys Crowd Funding platform.
This module defines the Category entity with its relationships and validation logic.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
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
            key: The name of the field being validated
            name: The category name value to validate
            
        Returns:
            str: The validated name
            
        Raises:
            ValueError: If the name is too short
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the category description meets minimum length requirements.
        
        Args:
            key: The name of the field being validated
            description: The description value to validate
            
        Returns:
            str: The validated description
            
        Raises:
            ValueError: If the description is too short
        """
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)
    
    def __repr__(self):
        """
        Returns a string representation of the Category instance.
        
        Returns:
            str: String representation showing category name
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
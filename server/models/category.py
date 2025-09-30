"""
Category model for the Tailspin Toys Crowd Funding platform.

This module defines the Category model for organizing games into
different genres or types.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Category(BaseModel):
    """
    Database model representing a game category.
    
    Attributes:
        id: Primary key identifier
        name: Name of the category
        description: Description of what games belong in this category
        games: Relationship to all games in this category
    """
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one category has many games
    games = relationship("Game", back_populates="category")
    
    @validates('name')
    def validate_name(self, key: str, name: str) -> str:
        """
        Validate category name meets length requirements.
        
        Args:
            key: Field name being validated
            name: Category name to validate
            
        Returns:
            Validated name string
            
        Raises:
            ValueError: If name is too short
        """
        return self.validate_string_length('Category name', name, min_length=2)
        
    @validates('description')
    def validate_description(self, key: str, description: str | None) -> str | None:
        """
        Validate category description meets length requirements.
        
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
        """Return string representation of the Category instance."""
        return f'<Category {self.name}>'
        
    def to_dict(self) -> dict:
        """
        Convert Category instance to dictionary for JSON serialization.
        
        Returns:
            Dictionary containing category data and game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
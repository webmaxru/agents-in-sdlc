"""
Game model for the Tailspin Toys Crowd Funding platform.
This module defines the Game data model with relationships to Publisher and Category models,
including validation and serialization methods.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Game(BaseModel):
    """
    Represents a game available for crowdfunding.
    
    Attributes:
        id (int): Unique identifier for the game
        title (str): Game title (2-100 characters)
        description (str): Detailed game description (minimum 10 characters)
        star_rating (float): User rating from 0-5 stars
        category_id (int): Foreign key reference to Category
        publisher_id (int): Foreign key reference to Publisher
        category: Relationship to Category model
        publisher: Relationship to Publisher model
    """
    __tablename__ = 'games'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Float, nullable=True)
    
    # Foreign keys for one-to-many relationships
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'), nullable=False)
    
    # One-to-many relationships (many games belong to one category/publisher)
    category = relationship("Category", back_populates="games")
    publisher = relationship("Publisher", back_populates="games")
    
    @validates('title')
    def validate_name(self, key, name):
        """
        Validate the game title field.
        
        Args:
            key (str): The field name being validated
            name (str): The title value to validate
            
        Returns:
            str: The validated title
            
        Raises:
            ValueError: If title is invalid (empty, wrong type, or too short)
        """
        return self.validate_string_length('Game title', name, min_length=2)
    
    @validates('description')
    def validate_description(self, key, description):
        """
        Validate the game description field.
        
        Args:
            key (str): The field name being validated
            description (str | None): The description value to validate
            
        Returns:
            str | None: The validated description
            
        Raises:
            ValueError: If description is invalid (wrong type or too short when provided)
        """
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    def __repr__(self):
        """
        Return a string representation of the Game instance.
        
        Returns:
            str: String representation showing game title and ID
        """
        return f'<Game {self.title}, ID: {self.id}>'

    def to_dict(self):
        """
        Convert the Game instance to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing game data with publisher and category info,
                 using camelCase for frontend compatibility (starRating)
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publisher': {'id': self.publisher.id, 'name': self.publisher.name} if self.publisher else None,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None,
            'starRating': self.star_rating  # Changed from star_rating to starRating
        }
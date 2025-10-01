"""
Game model for the Tailspin Toys Crowd Funding platform.
This module defines the Game model representing games available for crowdfunding,
with relationships to publishers and categories.
"""
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Game(BaseModel):
    """
    Represents a game available for crowdfunding.
    
    Attributes:
        id: Unique identifier for the game
        title: The title of the game
        description: Detailed description of the game
        star_rating: User rating from 0-5 stars
        category_id: Foreign key to the game's category
        publisher_id: Foreign key to the game's publisher
        category: Relationship to the Category model
        publisher: Relationship to the Publisher model
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
        Validates the game title meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            name: The title value to validate
            
        Returns:
            str: The validated title
        """
        return self.validate_string_length('Game title', name, min_length=2)
    
    @validates('description')
    def validate_description(self, key, description):
        """
        Validates the game description meets minimum length requirements.
        
        Args:
            key: The attribute key being validated
            description: The description value to validate
            
        Returns:
            str: The validated description
        """
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    def __repr__(self):
        """
        Returns a string representation of the Game instance.
        
        Returns:
            str: String representation showing title and ID
        """
        return f'<Game {self.title}, ID: {self.id}>'

    def to_dict(self):
        """
        Converts the Game instance to a dictionary for JSON serialization.
        
        Returns:
            dict: Dictionary containing game data with nested publisher and category info
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'publisher': {'id': self.publisher.id, 'name': self.publisher.name} if self.publisher else None,
            'category': {'id': self.category.id, 'name': self.category.name} if self.category else None,
            'starRating': self.star_rating  # Changed from star_rating to starRating
        }
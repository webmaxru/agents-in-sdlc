from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

class Publisher(BaseModel):
    """Model representing a game publisher."""
    __tablename__ = 'publishers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    # One-to-many relationship: one publisher has many games
    games = relationship("Game", back_populates="publisher")

    @validates('name')
    def validate_name(self, key, name):
        """Validate that publisher name meets minimum length requirements."""
        return self.validate_string_length('Publisher name', name, min_length=2)

    @validates('description')
    def validate_description(self, key, description):
        """Validate that publisher description meets minimum length requirements."""
        return self.validate_string_length('Description', description, min_length=10, allow_none=True)

    def __repr__(self):
        """Return string representation of Publisher."""
        return f'<Publisher {self.name}>'

    def to_dict(self):
        """
        Convert Publisher instance to dictionary representation.
        
        Returns:
            Dictionary containing publisher id, name, description, and game count
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'game_count': len(self.games) if self.games else 0
        }
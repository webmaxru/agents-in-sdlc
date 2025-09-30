"""
Base model providing shared validation methods for SQLAlchemy models.

This module defines the abstract base model that all database models inherit from,
providing common validation methods for string fields.
"""
# filepath: server/models/base.py
from . import db

class BaseModel(db.Model):
    """Abstract base model with common validation methods."""
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name: str, value: str | None, min_length: int = 2, allow_none: bool = False) -> str | None:
        """
        Validate that a string field meets length requirements.
        
        Args:
            field_name: Name of the field being validated (used in error messages)
            value: The string value to validate
            min_length: Minimum required length for the string (default: 2)
            allow_none: Whether None values are permitted (default: False)
            
        Returns:
            The validated string value or None if allow_none is True
            
        Raises:
            ValueError: If value is None and allow_none is False, if value is not a string,
                       or if value length is less than min_length
        """
        if value is None:
            if allow_none:
                return value
            else:
                raise ValueError(f"{field_name} cannot be empty")
        
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
            
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} must be at least {min_length} characters")
            
        return value
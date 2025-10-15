"""
Base model for the Tailspin Toys Crowd Funding platform.
This module defines the base model class with common validation methods.
"""
# filepath: server/models/base.py
from . import db

class BaseModel(db.Model):
    __abstract__ = True
    
    @staticmethod
    def validate_string_length(field_name, value, min_length=2, allow_none=False):
        """
        Validates that a string field meets minimum length requirements.
        
        Args:
            field_name: Name of the field being validated (for error messages)
            value: The string value to validate
            min_length: Minimum required length (default: 2)
            allow_none: Whether None values are allowed (default: False)
            
        Returns:
            str: The validated string value
            
        Raises:
            ValueError: If the value is None when not allowed, not a string, or too short
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
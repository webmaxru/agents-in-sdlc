"""
Models package for the Tailspin Toys Crowd Funding platform.
This package contains SQLAlchemy models for the database entities.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models after db is defined to avoid circular imports
from .category import Category
from .game import Game
from .publisher import Publisher
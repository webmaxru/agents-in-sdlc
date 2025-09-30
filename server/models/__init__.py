"""
Models package initialization for the Tailspin Toys Crowd Funding platform.

This package contains all SQLAlchemy database models and provides database
initialization functionality.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models after db is defined to avoid circular imports
from .category import Category
from .game import Game
from .publisher import Publisher

def init_db(app, testing: bool = False) -> None:
    """
    Initialize the database with the Flask application.
    
    Args:
        app: The Flask application instance
        testing: If True, allows reinitialization for testing
    """
    if testing:
        # For testing, we want to be able to reinitialize
        db.init_app(app)
    else:
        try:
            db.init_app(app)
        except RuntimeError:
            # Database already initialized
            pass
    
    # Create tables when initializing
    with app.app_context():
        db.create_all()
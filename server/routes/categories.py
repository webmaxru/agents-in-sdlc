"""
This file defines the Flask blueprint for category-related API endpoints.
It provides RESTful routes for retrieving category data from the database.
"""

from flask import jsonify, Response, Blueprint
from models import db, Category

# Create a Blueprint for categories routes
categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/api/categories', methods=['GET'])
def get_categories() -> Response:
    """
    Retrieve a list of all categories with their id and name.

    Returns:
        Response: JSON array of categories
    """
    categories = db.session.query(Category).all()
    categories_list = [
        {"id": category.id, "name": category.name}
        for category in categories
    ]
    return jsonify(categories_list)

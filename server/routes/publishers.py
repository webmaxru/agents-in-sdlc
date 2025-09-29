"""
This file defines the Flask blueprint for publisher-related API endpoints.
It provides RESTful routes for retrieving publisher data from the database.
"""

from flask import jsonify, Response, Blueprint
from models import db, Publisher

# Create a Blueprint for publishers routes
publishers_bp = Blueprint('publishers', __name__)

@publishers_bp.route('/api/publishers', methods=['GET'])
def get_publishers() -> Response:
    """
    Retrieve a list of all publishers with their id and name.

    Returns:
        Response: JSON array of publishers
    """
    publishers = db.session.query(Publisher).all()
    publishers_list = [
        {"id": publisher.id, "name": publisher.name}
        for publisher in publishers
    ]
    return jsonify(publishers_list)

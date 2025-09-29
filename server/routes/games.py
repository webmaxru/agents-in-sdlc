"""
Games API routes for the Tailspin Toys Crowd Funding platform.
This module provides endpoints to retrieve game information including details about
publishers and categories through RESTful API endpoints.
"""
from flask import jsonify, Response, Blueprint
from models import db, Game, Publisher, Category
from sqlalchemy.orm import Query

# Create a Blueprint for games routes
games_bp = Blueprint('games', __name__)

def get_games_base_query() -> Query:
    """
    Create a base SQLAlchemy query for games with joined publisher and category data.
    
    Returns:
        Query: SQLAlchemy query object with Game, Publisher, and Category joined
    """
    return db.session.query(Game).join(
        Publisher, 
        Game.publisher_id == Publisher.id, 
        isouter=True
    ).join(
        Category, 
        Game.category_id == Category.id, 
        isouter=True
    )

@games_bp.route('/api/games', methods=['GET'])
def get_games() -> Response:
    """
    Retrieve all games with their associated publisher and category information.
    
    Returns:
        Response: JSON response containing an array of game objects with publisher
                 and category details, star ratings, and descriptions
    """
    # Use the base query for all games
    games_query = get_games_base_query().all()
    
    # Convert the results using the model's to_dict method
    games_list = [game.to_dict() for game in games_query]
    
    return jsonify(games_list)

@games_bp.route('/api/games/<int:id>', methods=['GET'])
def get_game(id: int) -> tuple[Response, int] | Response:
    """
    Retrieve a specific game by its ID with associated publisher and category information.
    
    Args:
        id (int): The unique identifier of the game to retrieve
    
    Returns:
        tuple[Response, int] | Response: JSON response containing the game object,
                                        or 404 error response if game not found
    """
    # Use the base query and add filter for specific game
    game_query = get_games_base_query().filter(Game.id == id).first()
    
    # Return 404 if game not found
    if not game_query: 
        return jsonify({"error": "Game not found"}), 404
    
    # Convert the result using the model's to_dict method
    game = game_query.to_dict()
    
    return jsonify(game)

from flask import jsonify, Response, Blueprint, request
from models import db, Game, Publisher, Category
from sqlalchemy.orm import Query

# Create a Blueprint for games routes
games_bp = Blueprint('games', __name__)

def get_games_base_query() -> Query:
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
    # Use the base query for all games
    games_query = get_games_base_query().all()
    
    # Convert the results using the model's to_dict method
    games_list = [game.to_dict() for game in games_query]
    
    return jsonify(games_list)

@games_bp.route('/api/games/<int:id>', methods=['GET'])
def get_game(id: int) -> tuple[Response, int] | Response:
    # Use the base query and add filter for specific game
    game_query = get_games_base_query().filter(Game.id == id).first()
    
    # Return 404 if game not found
    if not game_query: 
        return jsonify({"error": "Game not found"}), 404
    
    # Convert the result using the model's to_dict method
    game = game_query.to_dict()
    
    return jsonify(game)

@games_bp.route('/api/games', methods=['POST'])
def create_game() -> tuple[Response, int]:
    """Create a new game"""
    # Get JSON data from request
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    required_fields = ['title', 'description', 'categoryId', 'publisherId']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    try:
        # Verify that category and publisher exist
        category = Category.query.get(data['categoryId'])
        if not category:
            return jsonify({"error": "Category not found"}), 404
        
        publisher = Publisher.query.get(data['publisherId'])
        if not publisher:
            return jsonify({"error": "Publisher not found"}), 404
        
        # Create new game
        new_game = Game(
            title=data['title'],
            description=data['description'],
            category_id=data['categoryId'],
            publisher_id=data['publisherId'],
            star_rating=data.get('starRating')  # Optional field
        )
        
        db.session.add(new_game)
        db.session.commit()
        
        # Return created game with 201 status
        return jsonify(new_game.to_dict()), 201
        
    except ValueError as e:
        # Handle validation errors from model validators
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to create game"}), 500

@games_bp.route('/api/games/<int:id>', methods=['PUT'])
def update_game(id: int) -> tuple[Response, int]:
    """Update an existing game"""
    # Get the game
    game = Game.query.get(id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    
    # Get JSON data from request
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        # Update fields if provided
        if 'title' in data:
            game.title = data['title']
        
        if 'description' in data:
            game.description = data['description']
        
        if 'categoryId' in data:
            category = Category.query.get(data['categoryId'])
            if not category:
                return jsonify({"error": "Category not found"}), 404
            game.category_id = data['categoryId']
        
        if 'publisherId' in data:
            publisher = Publisher.query.get(data['publisherId'])
            if not publisher:
                return jsonify({"error": "Publisher not found"}), 404
            game.publisher_id = data['publisherId']
        
        if 'starRating' in data:
            game.star_rating = data['starRating']
        
        db.session.commit()
        
        # Return updated game
        return jsonify(game.to_dict()), 200
        
    except ValueError as e:
        # Handle validation errors from model validators
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update game"}), 500

@games_bp.route('/api/games/<int:id>', methods=['DELETE'])
def delete_game(id: int) -> tuple[Response, int]:
    """Delete a game"""
    # Get the game
    game = Game.query.get(id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    
    try:
        db.session.delete(game)
        db.session.commit()
        return jsonify({"message": "Game deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete game"}), 500


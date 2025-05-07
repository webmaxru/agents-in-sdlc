import os
from models import init_db as models_init_db


def init_db(app):
    """
    Initializes the database with the given Flask app.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = __get_connection_string()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    models_init_db(app)

def __get_connection_string():
    """
    Returns the connection string for the database.
    """
    # Get the server directory
    server_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Go up one level to project root, then into data folder
    project_root = os.path.dirname(server_dir)
    data_dir = os.path.join(project_root, "data")
    
    # Create the data directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)
    
    return f'sqlite:///{os.path.join(data_dir, "tailspin-toys.db")}'
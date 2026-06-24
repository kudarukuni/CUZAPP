"""
Flask app factory
"""

from flask import Flask
from app.config import Config


def create_app():
    """Create and configure Flask app"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please set up your .env file with required Twilio credentials")
    
    # Register blueprints
    from app.routes import api_bp
    app.register_blueprint(api_bp)
    
    return app

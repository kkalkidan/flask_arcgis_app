from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Enable CORS for all routes
    CORS(app)
    
    # Register blueprints
    from app.routes.map_routes import map_bp
    from app.routes.main_routes import main_bp
    
    app.register_blueprint(map_bp, url_prefix='/map')
    app.register_blueprint(main_bp)
    
    return app
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # CORS(app, resources={r"/process_campaign": {"origins": "*"}})
    
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)
    
    return app

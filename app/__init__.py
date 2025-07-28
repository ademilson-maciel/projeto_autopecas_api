from flask import Flask
from app.database import db
from app.routes import register_routes

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pecas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "chave-secreta"

    db.init_app(app)

    with app.app_context():
        db.create_all()
        register_routes(app)
    
    return app
      
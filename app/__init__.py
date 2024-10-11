from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        from .models.user import Usuario
        return Usuario.query.get(int(user_id))

    from app.routes import auth, motos_routes, admin_routes

    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(motos_routes.bp)
    app.register_blueprint(admin_routes.bp)

    return app 
from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# Function to initialize the app
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key')

    # Set up the database
    engine = create_engine('mysql+mysqlconnector://root:Root%40123@localhost/movies_db')
    Session = sessionmaker(bind=engine)
    app.db_session = Session()

    # Register blueprints
    from .routes.home import home_bp
    from .routes.auth import auth_bp
    from .routes.tracker import tracker_bp
    from .routes.search import search_bp
    from .routes.user_menu import user_menu_bp


    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(tracker_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(user_menu_bp)

    return app

from flask import Blueprint, render_template, session
from models import Movie

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    from flask import current_app
    db_session = current_app.db_session

    user_id = session.get('user_id')
    if not user_id:
        return render_template('index.html')  # Show login/register options if not logged in

    # Query the list of 30 movies
    movies = db_session.query(Movie).limit(100).all()
    return render_template('movies.html', movies=movies)

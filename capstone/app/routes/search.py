from flask import Blueprint, render_template, request, redirect, url_for, session
from models import Genre, Movie, MovieTracker

search_bp = Blueprint('search', __name__)

@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    from flask import current_app
    db_session = current_app.db_session

    if request.method == 'POST':
        return redirect(url_for('tracker.tracker'))

    query = request.args.get('query')
    search_option = request.args.get('search_option')
    if search_option == '1':
        movies = db_session.query(Movie).filter(Movie.Title.ilike(f"%{query}%")).all()
    elif search_option == '2':
        movies = db_session.query(Movie).join(Genre).filter(Genre.Genre.ilike(f"%{query}%")).all()
    else:
        movies = []
    
    return render_template('search.html', movies=movies)

@search_bp.route('/add_to_tracker', methods=['POST'])
def add_to_tracker():
    from flask import current_app
    db_session = current_app.db_session

    user_id = session.get('user_id')
    movie_id = request.form.get('movie_id')
    status = request.form.get('status')

    if not user_id or not movie_id or not status:
        return "Missing form data", 400

    existing_entry = db_session.query(MovieTracker).filter_by(UserID=user_id, MovieID=movie_id).first()
    if existing_entry:

        # custom error

        query = request.args.get('query')  # Keep the search query
        search_option = request.args.get('search_option')
        movies = db_session.query(Movie).filter(Movie.Title.ilike(f"%{query}%")).all() if query else []
        return render_template('search.html', movies=movies, error="Movie already exists in your tracker.")
    
    new_entry = MovieTracker(UserID=user_id, MovieID=movie_id, Status=status)
    db_session.add(new_entry)
    db_session.commit()

    return redirect(url_for('tracker.tracker'))

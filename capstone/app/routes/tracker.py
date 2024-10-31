from flask import Blueprint, render_template, session, request, redirect, url_for
from models import Movie, MovieTracker, User

tracker_bp = Blueprint('tracker', __name__)

def rating_to_stars(rating):
    if rating is None:
        return "No Rating"
    # Ensure rating is clamped between 1 and 10
    clamped_rating = max(1, min(10, rating))
    # Convert the 10-point scale to a 5-star scale
    stars_count = int(clamped_rating / 2)  # Full stars (1-10 to 0-5)
    stars = '⭐️' * stars_count  # Full stars
    # empty_stars = '1/2' * (5 - stars_count)  # Empty stars
    return stars


@tracker_bp.route('/tracker')
def tracker():
    from flask import current_app
    db_session = current_app.db_session

    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    user = db_session.query(User).get(user_id)
    movie_tracker_entries = db_session.query(MovieTracker).filter_by(UserID=user.UserID).all()
    return render_template('tracker.html', user=user, movie_tracker_entries=movie_tracker_entries, rating_to_stars=rating_to_stars)

@tracker_bp.route('/delete_movie/<int:movie_id>', methods=['POST'])
def delete_movie(movie_id):
    from flask import current_app
    db_session = current_app.db_session
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    # Find the movie tracker entry to delete
    movie_tracker_entry = db_session.query(MovieTracker).filter_by(UserID=user_id, MovieID=movie_id).first()
    
    if movie_tracker_entry:
        db_session.delete(movie_tracker_entry)
        db_session.commit()
    
    return redirect(url_for('tracker.tracker'))

@tracker_bp.route('/update_status', methods=['GET', 'POST'])
def update_status():
    from flask import current_app
    db_session = current_app.db_session

    user_id = session.get('user_id')
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        new_status = request.form['status']

        movie_tracker_entry = db_session.query(MovieTracker).join(Movie).filter(
            MovieTracker.UserID == user_id,
            Movie.Title.ilike(f"%{movie_title}%")
        ).first()

        if movie_tracker_entry:
            movie_tracker_entry.Status = new_status
            db_session.commit()
            message = f"Status updated for '{movie_title}' to '{new_status}'."
            return render_template('update_status.html', message=message)
        else:
            # Custom error message if movie is not found in the tracker
            error_message = f"The movie '{movie_title}' is not in your tracker."
            return render_template('update_status.html', error=error_message)

    return render_template('update_status.html')

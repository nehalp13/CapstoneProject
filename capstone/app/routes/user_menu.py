from flask import Blueprint, redirect, render_template, session, url_for
from models import User

user_menu_bp = Blueprint('user_menu', __name__)

@user_menu_bp.route('/user_menu')
def user_menu():
    from flask import current_app
    db_session = current_app.db_session

    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))  # Redirect if the user is not logged in

    user = db_session.query(User).get(user_id)
    if not user:
        return redirect(url_for('auth.login'))  # Additional check for invalid user_id

    return render_template('user_menu.html', user=user)

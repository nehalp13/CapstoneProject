from flask import Blueprint, render_template, request, redirect, url_for, session
import re
from models import User

auth_bp = Blueprint('auth', __name__)

# Regex for password validation
PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

# Custom Exceptions
class InvalidCredentialsError(Exception):
    """Exception raised for invalid login credentials."""
    pass

class UsernameAlreadyExistsError(Exception):
    """Exception raised when attempting to register with a taken username."""
    pass

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    from flask import current_app
    db_session = current_app.db_session

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            # Check if user exists and password matches
            user = db_session.query(User).filter_by(Username=username, Password=password).first()
            if not user:
                raise InvalidCredentialsError("Invalid username or password")
            
            # If valid, create session
            session['user_id'] = user.UserID
            return redirect(url_for('home.home'))
        
        except InvalidCredentialsError as e:
            return render_template('login.html', error=str(e))
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    from flask import current_app
    db_session = current_app.db_session

    if 'user_id' in session:
        return redirect(url_for('home.home'))

    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']
            
            # Check if username already exists
            existing_user = db_session.query(User).filter_by(Username=username).first()
            if existing_user:
                raise UsernameAlreadyExistsError("Username already taken!")
            
            # Validate password
            if not re.match(PASSWORD_REGEX, password):
                raise ValueError("Password must be at least 8 characters long, include an uppercase letter, lowercase letter, digit, and special character.")

            # Add new user to database
            new_user = User(Username=username, Password=password)
            db_session.add(new_user)
            db_session.commit()
            
            # Automatically log the user in after registration
            session['user_id'] = new_user.UserID
            return redirect(url_for('home.home'))

        except UsernameAlreadyExistsError as e:
            return render_template('register.html', message=str(e))
        except ValueError as e:
            return render_template('register.html', message=str(e))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home.home'))

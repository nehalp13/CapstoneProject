# Movie Tracker Application

A Flask-based application for tracking movies, featuring user registration, login, and a comprehensive movie tracker.

Follow these instructions to set up and run the application on your local machine.

## Prerequisites

- Python 3.13 or higher
- Virtual environment (`venv`)
- Flask and required dependencies (as specified in `requirements.txt`)
- MySQL

## Project Setup Instructions

#### 1. Clone the Repository
To get started, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/nehalp13/CapstoneProject.git
cd CapstoneProject/capstone
```

#### 2. Set Up the MySQL Database Structure
Run the `movies_db.sql` script in your MySQL environment to create the database structure:

- To run the entire script, look for the lightning bolt icon (⚡) in the toolbar

#### 3. Insert Data into the Database
- Open the `Project.ipynb` Jupyter Notebook file and execute each cell to insert data into the newly created database.
- Before running the notebooks, update the database connection string in each notebook to reflect your username and password:
```python
engine = create_engine('mysql+mysqlconnector://username:password@localhost/movies_db')
```
- For example, if your credentials are as follows:
```python
engine = create_engine('mysql+mysqlconnector://root:Root%40123@localhost/movies_db')
```
Make sure to change the username and password according to your MySQL credentials.

## Installation

1. **Create and Activate a Virtual Environment**:
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

2. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database Connection**:
   - Open `config.py` and `app/__init__.py`, and set your database connection string:
     ```python
     # MySQL connection string
     SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/movies_db'
     ```
   - Ensure that the connection string in `app/__init__.py` matches what you set in `config.py`.

4. **Generate a Random Secret Key**:
   Run the following command in the terminal to generate a random secret key:
   ```bash
   python secret.py
   ```
   The output will be a random secret key (a byte string) to use in your Flask application.

5. **Set the Secret Key in Your Flask App**:
   - On macOS/Linux:
     ```bash
     export SECRET_KEY="your_generated_secret_key"  # Replace with the output from secret.py
     ```
   - On Windows:
     ```bash
     set SECRET_KEY="your_generated_secret_key"      # For current session
     ```
     To set it permanently:
     ```bash
     setx SECRET_KEY "your_generated_secret_key"
     ```

## Running the Application

1. **Set Environment Variables**:
   - On macOS/Linux:
     ```bash
     export FLASK_APP=run.py
     export FLASK_DEBUG=1
     ```
   - On Windows:
     ```bash
     set FLASK_APP=run.py
     set FLASK_DEBUG=1
     ```

2. **Start the Flask Development Server**:
   ```bash
   flask run
   ```
   If port 5000 is already in use, specify an alternative port:
   ```bash
   flask run --port 5001
   ```

3. **Access the Application**:
   Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

## Usage

- **Register** for an account if you’re a new user.
- **Login** with your credentials to access and update your movie tracker.
- **Add, delete, or update movie status** as you track your movie-watching progress.

## Features

- **User Registration and Login** with password validation.
- **Movie Tracker**: Add movies to monitor their completion status.
- **Custom Error Handling** for:
  - Duplicate movie entries.
  - Attempting to update a movie not present in the tracker.

## Custom Exceptions in auth.py File

1. **InvalidCredentialsError**: Raised if the login credentials are incorrect, displaying an error message on the login page.
2. **UsernameAlreadyExistsError**: Raised during registration if a user tries to register with a taken username.
3. **ValueError**: Raised if the password does not meet regex validation requirements.

## Additional Notes
- Ensure that your database credentials are correct and update them in the necessary files.
- Don't forget to set and export the secret key before running the Flask app.

## Customization
- Update `username` and `password` with your actual MySQL credentials in all Python notebooks in `Project.ipynb`, as well as in the Flask app files such as `config.py` and `app/__init__.py`.
- Replace `your_generated_secret_key` with the key obtained after running `secret.py` and export it accordingly.

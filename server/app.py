# server/app.py

from flask import Flask
from flask_migrate import Migrate

from models import db, Pet  # Import db and the Pet model

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask application to use the database
db.init_app(app)

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Welcome to the Pet App! Use the Flask shell to interact with the database."

if __name__ == '__main__':
    app.run(port=5555, debug=True)

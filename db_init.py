import os
import dotenv
dotenv.load_dotenv()

ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

# Import the 'db' object and the 'User' model class from the 'app' module.
from app import app, db
from app import User, Analysis

# Need to set up application context while using the db functions
with app.app_context():
	# delete User table
	db.drop_all()

	# Create all the tables defined in the app's models.
	# If tables already exist, this won't recreate them.
	db.create_all()

	# Delete existing admin user
	User.query.filter_by(username='admin').delete()

	# Create a new user instance with the username 'admin' and the hashed password.
	new_user = User(username='admin')
	new_user.set_password(ADMIN_PASSWORD)

	# Add the new user instance to the current session's staging area.
	# This prepares it to be stored in the database.
	db.session.add(new_user)

	# Commit the changes made in the session to the database.
	# This will save the new user in the 'users' table.
	db.session.commit()
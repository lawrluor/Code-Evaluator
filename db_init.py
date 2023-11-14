# Import the 'db' object and the 'User' model class from the 'app' module.
from app import app, db, User

# Import the 'generate_password_hash' function from the 'werkzeug.security' module.
# This function is used to create a hashed version of a password.
from werkzeug.security import generate_password_hash

# Need to set up application context while using the db functions
with app.app_context():
	# Create all the tables defined in the app's models.
	# If tables already exist, this won't recreate them.
	db.create_all()

	# Generate a hashed version of the string 'password123' using the scrypt hashing algorithm.
	hashed_pw = generate_password_hash('password123', method='scrypt')

	# Create a new user instance with the username 'admin' and the hashed password.
	new_user = User(username='admin', password=hashed_pw)

	# Add the new user instance to the current session's staging area.
	# This prepares it to be stored in the database.
	db.session.add(new_user)

	# Commit the changes made in the session to the database.
	# This will save the new user in the 'users' table.
	db.session.commit()

	# delete all users
	# User.query.delete()
"""Seed file to make sample data for pets db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
joey = User(first_name='Joey', last_name='Houser', profile_image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdLHGdyMZvBFR42XDWnF5GUcBD9zshSnKVSg&usqp=CAU")
mary = User(first_name='Mary', last_name='Simpson', profile_image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJZG-8Pk5VYr_MOP4Ks3uEeZdArTUAizNRwg&usqp=CAU")
lisa = User(First_name='Lisa', last_name='McDonald')

# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)
db.session.add(spike)

# Commit--otherwise, this never gets saved!
db.session.commit()
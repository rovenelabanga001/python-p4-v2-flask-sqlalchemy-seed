#!/usr/bin/env python3
#server/seed.py

from app import app
from models import db, Pet

from random import choice as rc
from faker import Faker

with app.app_context():

    #Delete all rows in the "pets" table
    # Pet.query.delete()

    # # Create an empty list
    # pets = []

    # # Add some Pet instances to the list
    # pets.append(Pet(name = "Fido", species = "Dog"))
    # pets.append(Pet(name = "Whiskers", species = "Cat"))
    # pets.append(Pet(name = "Hermie", species = "Hamster"))
    # pets.append(Pet(name = "Slither", species = "Snake"))

    fake = Faker()

    Pet.query.delete()

    pets = []

    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    for n in range(10):
        pet = Pet(name=fake.first_name(), species = rc(species))
        pets.append(pet)


    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()
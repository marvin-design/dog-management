from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Dog, Owner

engine = create_engine('sqlite:///dog.db')
Session = sessionmaker(bind=engine)
session = Session()

def list_dogs():
    dogs = session.query(Dog).all()
    for dog in dogs:
        print(f"{dog.id}: {dog.name} ({dog.breed}) - Owner: {dog.owner.name}")

def add_dog():
    name = input("Dog's name: ")
    breed = input("Breed: ")
    age = int(input("Age: "))
    owner_name = input("Owner's name: ")

    owner = session.query(Owner).filter_by(name=owner_name).first()
    if not owner:
        owner = Owner(name=owner_name)
        session.add(owner)
        session.commit()

    dog = Dog(name=name, breed=breed, age=age, owner=owner)
    session.add(dog)
    session.commit()
    print(f"Added {name}.")

def delete_dog():
    list_dogs()
    dog_id = int(input("Enter ID of dog to delete: "))
    dog = session.query(Dog).get(dog_id)
    if dog:
        session.delete(dog)
        session.commit()
        print("Dog deleted.")
    else:
        print("Dog not found.")

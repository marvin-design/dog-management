from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Dog, Owner, ActivityLog, HealthRecord
from datetime import datetime

# Setup DB session
engine = create_engine('sqlite:///dog.db')
Session = sessionmaker(bind=engine)
session = Session()

def list_dogs():
    dogs = session.query(Dog).all()
    if not dogs:
        print("No dogs found.")
        return
    for dog in dogs:
        print(f"{dog.id}: {dog.name} ({dog.breed}, Age {dog.age}) - Owner: {dog.owner.name}")

def add_dog():
    name = input("Dog's name: ")
    breed = input("Breed: ")
    age = int(input("Age: "))
    medical_notes = input("Medical history/notes (optional): ")
    owner_name = input("Owner's name: ")

    owner = session.query(Owner).filter_by(name=owner_name).first()
    if not owner:
        owner = Owner(name=owner_name)
        session.add(owner)
        session.commit()

    dog = Dog(name=name, breed=breed, age=age, medical_notes=medical_notes, owner=owner)
    session.add(dog)
    session.commit()
    print(f"Added {name}.")

def delete_dog():
    list_dogs()
    try:
        dog_id = int(input("Enter ID of dog to delete: "))
    except ValueError:
        print("Invalid ID.")
        return
    dog = session.query(Dog).get(dog_id)
    if dog:
        session.delete(dog)
        session.commit()
        print("Dog deleted.")
    else:
        print("Dog not found.")

def log_activity():
    list_dogs()
    try:
        dog_id = int(input("Enter ID of dog to log activity for: "))
    except ValueError:
        print("Invalid ID.")
        return
    dog = session.query(Dog).get(dog_id)
    if not dog:
        print("Dog not found.")
        return

    activity_type = input("Activity type (e.g., Walk, Play, Bath): ")
    notes = input("Notes (optional): ")

    activity = ActivityLog(dog=dog, activity_type=activity_type, notes=notes)
    session.add(activity)
    session.commit()
    print(f"Activity logged for {dog.name}.")

def view_activities():
    list_dogs()
    try:
        dog_id = int(input("Enter ID of dog to view activities: "))
    except ValueError:
        print("Invalid ID.")
        return
    dog = session.query(Dog).get(dog_id)
    if not dog:
        print("Dog not found.")
        return

    activities = dog.activities
    if not activities:
        print("No activities recorded.")
    else:
        for a in activities:
            print(f"{a.timestamp.strftime('%Y-%m-%d %H:%M')} - {a.activity_type}: {a.notes or 'No notes'}")

def log_health_record():
    list_dogs()
    try:
        dog_id = int(input("Enter ID of dog to log health record for: "))
    except ValueError:
        print("Invalid ID.")
        return
    dog = session.query(Dog).get(dog_id)
    if not dog:
        print("Dog not found.")
        return

    record_type = input("Record type (e.g., Vaccination, Medication): ")
    description = input("Description: ")
    try:
        date_input = input("Date (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return
    notes = input("Notes (optional): ")

    record = HealthRecord(dog=dog, record_type=record_type, description=description, date=date, notes=notes)
    session.add(record)
    session.commit()
    print(f"Health record logged for {dog.name}.")

def view_health_records():
    list_dogs()
    try:
        dog_id = int(input("Enter ID of dog to view health records: "))
    except ValueError:
        print("Invalid ID.")
        return
    dog = session.query(Dog).get(dog_id)
    if not dog:
        print("Dog not found.")
        return

    records = dog.health_records
    if not records:
        print("No health records available.")
    else:
        for r in records:
            print(f"{r.date.strftime('%Y-%m-%d')} - {r.record_type}: {r.description} ({r.notes or 'No notes'})")

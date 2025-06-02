from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Owner, Dog, ActivityLog, HealthRecord

# Connect to the database
engine = create_engine('sqlite:///lib/db/app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Recreate tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create owners
owner1 = Owner(name="Alice")
owner2 = Owner(name="Bob")

# Create dogs
dog1 = Dog(name="Buddy", breed="Golden Retriever", age=3, owner=owner1)
dog2 = Dog(name="Charlie", breed="Poodle", age=5, owner=owner1)
dog3 = Dog(name="Daisy", breed="Bulldog", age=4, owner=owner2)

# Add and commit owners and dogs
session.add_all([owner1, owner2, dog1, dog2, dog3])
session.commit()

# Add activity logs
activities = [
    ActivityLog(activity_type="Walk", notes="30-minute walk", dog=dog1),
    ActivityLog(activity_type="Meal", notes="Dry food breakfast", dog=dog1),
    ActivityLog(activity_type="Play", notes="Fetch in the yard", dog=dog2),
]

# Add health records
records = [
    HealthRecord(record_type="Vaccination", description="Rabies shot", dog=dog1),
    HealthRecord(record_type="Medication", description="Heartworm meds", dog=dog2),
]

# Add and commit logs
session.add_all(activities + records)
session.commit()

# Print confirmation
print("Database seeded with dogs, owners, activities, and health records.")

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.db.base import Base  



class ActivityLog(Base):
    __tablename__ = 'activity_logs'

    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    activity_type = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    dog = relationship("Dog", back_populates="activities")

class HealthRecord(Base):
    __tablename__ = 'health_records'

    id = Column(Integer, primary_key=True)
    dog_id = Column(Integer, ForeignKey('dogs.id'))
    record_type = Column(String)  # e.g., "Vaccination", "Medication"
    description = Column(String)
    date = Column(DateTime)
    notes = Column(String)

    dog = relationship("Dog", back_populates="health_records")

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String)
    age = Column(Integer)
    medical_notes = Column(Text)  # <-- new field for medical history/notes
    owner_id = Column(Integer, ForeignKey('owners.id'))

    owner = relationship("Owner", back_populates="dogs")
    activities = relationship("ActivityLog", back_populates="dog", cascade="all, delete")
    health_records = relationship("HealthRecord", back_populates="dog", cascade="all, delete")
class Owner(Base):
    __tablename__ = 'owners'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    dogs = relationship("Dog", back_populates="owner", cascade="all, delete")

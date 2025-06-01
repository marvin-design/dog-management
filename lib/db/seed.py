from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Owner, Dog, Vaccination

engine = create_engine('sqlite:///dog.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    owner1 = Owner(name='Nancy')
    dog1 = Dog(name='Rex', breed='German Shepherd', age=3, owner=owner1)
    dog2 = Dog(name='Luna', breed='Labrador', age=5, owner=owner1)

    vac1 = Vaccination(name='Rabies', dog=dog1)
    vac2 = Vaccination(name='Parvo', dog=dog2)

    session.add_all([owner1, dog1, dog2, vac1, vac2])
    session.commit()
    print("Seed complete!")

if __name__ == '__main__':
    seed()

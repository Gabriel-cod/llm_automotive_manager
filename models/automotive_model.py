from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from faker import Faker
from random import choice, randint
from settings import DATABASE_URL


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def db_dependency(func):
    def wrapper(*args, **kwargs):
        db = SessionLocal()
        try:
            result = func(*args, _db=db, **kwargs)
        finally:
            db.close()
            return result
    return wrapper

@db_dependency
def populate_db_with_fictitious_data(_db: Session):
    fake = Faker("pt_BR")
    auxiliary_brands = {
        'Toyota': [('Corolla', 'Sedan'), ('Yaris', 'Hatch'), ('Yaris', 'Sedan'), ('SW4', 'SUV'), ('Hillux', 'Pickup')],
        'Honda': [('City', 'Sedan'), ('Civic', 'Sedan'), ('Accord', 'Sedan')], 
        'Ford': [('Ecosport', 'SUV'), ('Fusion', 'Sedan'), ('Fiesta', 'Hatch'), ('Ka', 'Hatch'), ('Ranger', 'Pickup')],
        'Chevrolet': [('Cruze', 'Hatch'), ('Onix', 'Sedan'), ('Onix', 'Hatch'), ('Celta', 'Hatch'), ('Cruze', 'Hatch'), ('S10', 'Pickup')],
        'Fiat': [('Toro', 'Pickup'), ('Siena', 'Sedan'), ('Palio', 'Hatch'), ('Argo', 'Hatch'), ('Uno', 'Hatch')]
    }
    for _ in range(100):
        brand = choice(list(auxiliary_brands.keys()))
        car = choice(auxiliary_brands[brand])
        model = car[0]
        category = car[1]
        new_car = Car(
            brand=brand,
            model=model,
            color=fake.color_name(),
            factory_year=fake.year(),
            category=category,
            fuel_type=choice(['Gasolina', 'Diesel', 'Flex']),
            license_plate=fake.license_plate(),
            seating_capacity=randint(2, 5),
            doors=randint(2, 4),
            daily_rate=randint(300, 620),
            available=choice([True, False])
        )
        _db.add(new_car)
    _db.commit()
    _db.close()


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    color = Column(String, nullable=False)
    factory_year = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    fuel_type = Column(String, nullable=False)
    license_plate = Column(String, nullable=False)
    seating_capacity = Column(Integer, nullable=False)
    doors = Column(Integer, nullable=False)
    daily_rate = Column(Float(2), nullable=False)
    available = Column(Boolean,  nullable=False)

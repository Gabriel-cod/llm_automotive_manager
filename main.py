from models.automotive_model import Base, engine
from server.db_tools import search_cars

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    search_cars("SELECT * FROM cars WHERE brand = 'Mercedes';")
    
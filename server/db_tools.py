from fastmcp import FastMCP
from models.automotive_model import db_dependency
from sqlalchemy.orm import Session
from sqlalchemy import text


mcp_server = FastMCP("automotive_manager")

@mcp_server.tool
@db_dependency
def search_cars(query: str, _db: Session = None) -> list:
    """
    Use this function to search for cars in the 'cars' table of the database with a SELECT query.
    Your query should look like this: SELECT * FROM cars WHERE ...
    WHERE clause is optional
    You can search for cars using the following columns as filters:
        brand: str
        model: str
        color: str
        factory_year: int
        category: str
        fuel_type: str
        license_plate: str
        seating_capacity: int
        doors: int
        daily_rate: float
        available: bool

    Args:
        _db (Session): this parameter should not be informed
        query (str): must be a SQL SELECT query with WHERE clause if necessary

    Returns:
        list: the result of the query as a list of tuples, or empty list if there is no result, containing the following columns:
        (id, brand, model, color, factory_year, category, fuel_type, license_plate, seating_capacity, doors, daily_rate, available: bool -> 0 or 1)
    """
    result = _db.execute(text(query)).all()
    return result

if __name__ == '__main__':
    mcp_server.run('stdio')

from langchain_openai import ChatOpenAI
from langchain.tools import BaseTool
from langchain.agents import initialize_agent, AgentType
from fastmcp import Client
from typing import Type
from pydantic import BaseModel, Field
from settings import mcp_server_path
import asyncio


class SearchCarsDBInput(BaseModel):
    query: str = Field(description="SQL query to search for cars in the database")


class SearchCarsDBTool(BaseTool):
    name: str = "search_cars"
    description: str = """
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
    args_schema: Type[BaseModel] = SearchCarsDBInput
    
    def _run(self, query: str) -> str:
        return asyncio.run(self._arun(query))
    
    async def _arun(self, query: str) -> str:
        async with Client(mcp_server_path) as client:
            result = await client.call_tool("search_cars", {"query": query})
            return str(result[0].text)



llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key="<<YOUR OPENAI API KEY>>")

agent = initialize_agent(
    tools=[SearchCarsDBTool()],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

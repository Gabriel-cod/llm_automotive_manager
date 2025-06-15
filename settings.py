from os import path
from pathlib import Path

DATABASE_URL = "sqlite:///./automotive_manager.db"
mcp_server_path = path.join(Path(__file__).parent, 'server', 'db_tools.py')

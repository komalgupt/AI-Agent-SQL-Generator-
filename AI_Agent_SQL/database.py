from sqlalchemy import create_engine, text
import pandas as pd

# 🔹 Update with actual database details
DATABASE_URL = "postgresql://user:password@localhost/dbname" #replace with your postgre credential 

# ✅ Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# ✅ Function to get a database connection
def get_connection():
    return engine.connect()

# ✅ Function to execute an SQL query
def execute_sql(sql_query):
    """Executes the given SQL query and returns results as JSON."""
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))  # Using `text()` for proper execution
            data = result.mappings().all()  # Fetch results as dictionaries
            return [dict(row) for row in data] if data else []
    except Exception as e:
        return {"error": str(e)}

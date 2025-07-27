import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 🔥 FIX: Ensure DATABASE_URL is loaded correctly
DATABASE_URL = os.getenv("DB_URI")
if not DATABASE_URL:
    raise ValueError("Missing DATABASE_URL. Check your .env file!")

# 🔥 FIX: Initialize database engine
engine = create_engine(DATABASE_URL)

def execute_sql(sql_query):
    """Executes a secure SQL query and returns results as JSON."""
    try:
        # 🔥 FIX: Remove unnecessary backticks from Gemini-generated SQL
        sql_query = sql_query.strip().replace("```sql", "").replace("```", "")

        with engine.connect() as conn:
            result = pd.read_sql(sql_query, conn)
            return result.to_dict(orient="records")  # Convert DataFrame to JSON
    except Exception as e:
        return {"error": str(e)}

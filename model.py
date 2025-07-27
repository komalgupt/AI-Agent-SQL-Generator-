import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables (safe for local dev)
load_dotenv()

# ✅ Correct key name
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY. Check your .env file or Render settings!")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def convert_to_sql(user_query):
    """Convert natural language to SQL using Gemini AI."""
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    response = model.generate_content(f"Convert this natural language query to SQL: {user_query}")

    # Clean the response
    sql_query = response.text.strip().replace("```sql", "").replace("```", "")
    return sql_query

import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="your_API_Key")  #past your gemini API key here 

def convert_to_sql(user_query):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    # Ensure query starts with "Show" if needed
    if not user_query.lower().startswith("show"):
        user_query = "Show " + user_query

    prompt = (
        f"Convert this natural language query into a valid PostgreSQL query: \n"
        f"Natural Language Query: '{user_query}'\n"
        f"Output SQL query, without explanations, markdown, or comments."
    )

    response = model.generate_content(prompt)

    # Clean the response (Remove markdown SQL formatting)
    sql_query = response.text.replace("```sql", "").replace("```", "").strip()

    # Fix common issues (Example: Replacing incorrect column names)
    sql_query = sql_query.replace("hire_date", "joining_date")  # Fix column names

    return sql_query

# AI-Agent-SQL-Generator-

## Overview
This project is an AI-powered agent that translates natural language queries into SQL queries, executes them on a PostgreSQL database, and returns structured results. It enables users to interact with databases without requiring SQL expertise.

## Features
- **Natural Language to SQL Conversion:** Uses Google Gemini AI to convert user queries into SQL.
- **Query Execution & Result Processing:** Executes SQL queries on PostgreSQL and returns results in JSON or tabular format.
- **Error Handling & Optimization:** Detects incorrect or ambiguous queries, suggests corrections, and optimizes performance.
- **Web Interface:** Provides a user-friendly interface using Flask to submit queries and view results.

## Requirements
To set up and run the project, install the following dependencies:

```sh
pip install flask sqlalchemy psycopg2 google-generativeai pandas
```

## Project Structure
```
AI_SQL_Agent/
│-- app.py                # Flask web application
│-- model.py              # AI-powered natural language to SQL conversion
│-- database.py           # PostgreSQL database connection and query execution
│-- templates/
│   └── index.html        # Frontend UI for user interaction
|-- static/
|   └── styles.css
|-- DB_created_in_postgre.csv   #database which have been created in postgre SQL inserted here for reference purpose 
└── requirement.txt            
```

## Setup Instructions
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/komalgupt/AI_SQL_Agent.git
   cd AI_SQL_Agent
   ```

2. **Set Up PostgreSQL Database:**
   - Ensure PostgreSQL is installed and running.
   - Update `DATABASE_URL` in `database.py` with your database credentials:
     ```python
     DATABASE_URL = "postgresql://your_username:your_password@localhost/your_database"
     ```

3. **Run the Application:**
   ```sh
   python app.py
   ```
   The application will start on `http://127.0.0.1:5000/`.

## Security Notice  
⚠️ **Important:** This repository does not contain actual API keys or database credentials. Before running the project, update the following:  

1. Replace `"your_api_key"` in `model.py` with your actual Google Gemini API key.  
2. Update the database connection string in `database.py` as shown above.  
3. Consider using environment variables (`.env` file) for enhanced security instead of hardcoding credentials in the script.  

## Usage Guide
- **Enter a query in natural language** (e.g., "Show me employees who joined after 2020").
- **AI converts it into SQL** and executes it.
- **Results are displayed** in tabular format on the web interface.

## Deployment (Optional)
If you plan to deploy the application, you can use cloud platforms like AWS, Azure, or Heroku.

## Contribution
Feel free to contribute by submitting pull requests. Ensure your code is well-documented and follows best practices.

## License
This project is open-source and available.


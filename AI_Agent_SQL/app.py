from flask import Flask, request, jsonify, render_template
from model import convert_to_sql
from database import execute_sql
import os
from datetime import datetime, date

# Set the correct template folder path
TEMPLATE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    nl_query = data.get("query", "")

    if not nl_query:
        return jsonify({"error": "No query provided"}), 400

    # Convert NL to SQL
    sql_query = convert_to_sql(nl_query)
    #print(f"Generated SQL Query: {sql_query}")  # Debugging purpose
    print(f"Generated SQL Query: {sql_query}")  # Debugging


    try:
        results = execute_sql(sql_query)
        print(f"Query Results: {results}")  # Debugging: Check if results exist
    except Exception as e:
        return jsonify({"error": f"SQL Execution Error: {str(e)}"}), 500

    if not results or len(results) == 0:  
        return jsonify({"query": nl_query, "sql_query": sql_query, "table": "<p>No results found.</p>"})

    return jsonify({
        "query": nl_query,
        "sql_query": sql_query,
        "table": format_results_as_table(results)
    })


def format_results_as_table(results):
    """Convert query results into an HTML table format, handling empty results."""
    if not results:
        return "<p>No results found.</p>"  # Prevents KeyError when results are empty

    table_html = "<table border='1'><tr>{}</tr>{}</table>".format(
        "".join(f"<th>{key}</th>" for key in results[0].keys()),  # Uses column names as headers
        "".join(
            "<tr>" + "".join(f"<td>{format_value(value)}</td>" for value in row.values()) + "</tr>"
            for row in results
        ),
    )
    return table_html

def format_value(value):
    """Convert None to 'N/A' and format dates properly."""
    if value is None:
        return "N/A"
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    return value



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

# Text-to-SQL-System
A secure multidatabase tSQL system that converts user text into an SQL query which then the output of the SQL query is displayed to the user as text

## Features
Connects to multiple databases(Postgres, MySQL, BigQuery etc,
Secure SQL validation (read-only, table whitelist, enforced LIMIT)

## Project Structure
text-to-sql-system/
├── .env                  # DB connection strings and secrets
├── main.py               # API endpoints (included in app.py)
└── frontend/
    └── app.py            # Streamlit UI

## Quickstart Guide
1. **Install dependencies**
   
   `pip install -r requirements.txt
pip install streamlit sqlalchemy sqlglot python-dotenv requests python-dotenv llama index nltk sqlalchemy psycopg2 huggingface`

3. **Configure your database**

   Add DB URIs to .env as `DB_PROD_WAREHOUSE=..., DB_CRM_DB=..., etc.`

5. **Run frontend & backend**:

   `streamlit run app.py`

7. **Open the UI**

   Go to `http://localhost:8501` in your browser of choice.

9. **Interact with the LLM**

   Interact with the LLM by posting a prompt for inquiries on the DB.


## Security
Only allows SELECT queries

Only whitelisted tables per DB

Enforces LIMIT on all queries

Read-only DB connections where possible

## Next Steps

Split app.py into main.py and app.py for further development

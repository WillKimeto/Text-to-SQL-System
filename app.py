import streamlit as st
import os

from dotenv import load_dotenv
from llama_index.core.response.pprint_utils import pprint_response
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import SQLDatabase, Settings
from llama_index.core.indices.struct_store import NLSQLTableQueryEngine

from sqlalchemy import create_engine

load_dotenv()

storage_path = "./vectorstare"

# ✅ GROQ LLM SETUP
llm = Groq(
    model="openai/gpt-oss-20b",  # you can change this model
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.0
)

# Register LLM globally in LlamaIndex
Settings.llm = llm
Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Database connection
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/Amazon"
)

sql_database = SQLDatabase(engine, include_tables=["products", "sales"])

query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    tables=["products", "sales"],
    verbose=True
)

def queryDB(query_str):
    response = query_engine.query(query_str)
    return response


# ---------------- STREAMLIT UI ----------------
st.title("Query the database - TEXT to SQL ")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi!, I'm your Database Assistant. Ask me anything related to your database and i'll do my best to help you."}
    ]

if prompt := st.chat_input("Your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt and st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = queryDB(prompt)

            st.write(response.response)
            pprint_response(response, show_source=True)

            message = {
                "role": "assistant",
                "content": response.response
            }
            st.session_state.messages.append(message)

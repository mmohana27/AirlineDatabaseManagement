import streamlit as st
import mysql.connector

# Function to create a MySQL database connection
def create_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="abc",
        database="AIRLINEDBMS"
    )

# Function to execute SQL queries
def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    return result

# Streamlit app
def sql_query():
    # st.title("Airline DBMS SQL Query Executor6000")

    # Create a database connection
    connection = create_db_connection()

    # User input for SQL query
    x = st.sidebar.text_area("Enter SQL Query:")

    if st.sidebar.button("Execute Query"):
        result = execute_query(connection, x)
        if result:
            st.sidebar.write(result)
        else:
            st.sidebar.warning("No results or an error occurred.")

    # Close the database connection when Streamlit app is closed
    connection.close()

if __name__ == "__main__":
    sql_query()

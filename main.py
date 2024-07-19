import streamlit as st
import mysql.connector
import pandas as pd
import subprocess
# from emp import employee
# from admin import administrator
# from sql import sql_query

def insert_user_details(username, password, name, email, phno, role,is_admin):
    connection = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="AIRLINEDBMS"
    )

    cursor = connection.cursor()

    # Insert user details into the Employee table
    query = f"INSERT INTO Employee (username, password, name, email, phno, role, is_admin) " \
            f"VALUES ('{username}', '{password}', '{name}', '{email}', '{phno}', '{role}', {is_admin})"

    cursor.execute(query)
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


def authenticate(username, password):
    connection = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="AIRLINEDBMS"
    )

    cursor = connection.cursor()
    query = f"SELECT * FROM Employee WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

def login_register():
    st.title("Login / Register Page")

    # Create a database connection for SQL Query Executor sidebar
    connection_sidebar = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="AIRLINEDBMS"
    )

    option = st.radio("Choose an option:", ("Login", "Register"))

    if option == "Login":
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

        if st.button("Login"):
            user_data = authenticate(username, password)
            if user_data:
                role = user_data[7]
                if role == 'admin':
                    st.success("Login Successful as Admin!")
                    st.balloons()
                    admin_page_url = "xyz"  # Change the port if needed
                    st.markdown(f"Go to [Admin Page]({admin_page_url})")
                    # subprocess.Popen(["streamlit", "run", "admin.py", "--server.port", "8501"])
                else:
                    st.success("Login Successful as Employee!dash")
                    employee_page_url = "xyz"  # Change the port if needed
                    st.markdown(f"Go to [Employee Page]({employee_page_url})")
                    # subprocess.Popen(["streamlit", "run", "emp.py", "--server.port", "8502"])
            else:
                st.error("Invalid username or password. Please try again.")

    elif option == "Register":
        st.write("Fill in the details to register:")
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        phno = st.text_input("Phone Number:")
        role = st.selectbox("Select Role:", ["admin", "pilot", "attendant", "mechanic", "ground staff"])
        is_admin = st.checkbox("Is Admin")

        if st.button("Register"):
            # Add code to insert user details into the database
            insert_user_details(username, password, name, email, phno, role, is_admin)
            st.success("Registration Successful! You can now login.")

    # Close the database connection for SQL Query Executor sidebar when Streamlit app is closed
    connection_sidebar.close()

if __name__ == "__main__":
    login_register()

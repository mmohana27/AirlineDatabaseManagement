import streamlit as st
import pandas as pd
import mysql.connector


def create_connection():
    connection = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="airlinedbms"
    )
    return connection

def execute_query(query, values=None, fetchone=False):
    connection = create_connection()
    cursor = connection.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)

    result = None
    if fetchone:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()

    cursor.close()
    connection.commit()
    connection.close()

    return result

def count_assigned_tasks(employee_id):
    query = "SELECT count_assigned_tasks(%s)"
    values = (employee_id,)

    # Execute the query
    result = execute_query(query, values, fetchone=True)
    return result[0] if result else 0

def sql_query():
    connection = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="AIRLINEDBMS"
    )

    # User input for SQL query
    x = st.sidebar.text_area("Enter SQL Query:")

    if st.sidebar.button("Execute Query"):
        statements = x.split(';')
        cursor = connection.cursor()

        results = []
        errors = []

        try:
            for statement in statements:
                statement = statement.strip()
                if statement:
                    cursor.execute(statement)

                    # Check if it's a SHOW statement
                    if statement.strip().upper().startswith("SHOW"):
                        result = cursor.fetchall()  # Fetch the results for SHOW
                        results.append(result)
                    elif statement.strip().upper().startswith("SELECT"):
                        result = cursor.fetchall()
                        results.append(result)

            # Fetch any remaining results to avoid the "Unread result found" error
            cursor.fetchall()
        except Exception as e:
            connection.rollback()
            errors.append(str(e))
        finally:
            cursor.close()
            connection.close()

        if results:
            st.sidebar.write(results)
        elif errors:
            st.sidebar.error(f"Error: {', '.join(errors)}")
        else:
            st.sidebar.warning("No results or an error occurred.")


#admin main page
st.title("Airline Management System Admin Page")
# Sidebar
st.sidebar.title("SQL Query Executor6000")
sql_query()

operations = [
    "Create Airport", "Read Airports", "Update Airport", "Delete Airport",
    "Create Employee", "Read Employees", "Update Employee", "Delete Employee",
    "Create Task", "Read Tasks", "Update Task", "Delete Task",
    "Create Flight", "Read Flights", "Update Flight", "Delete Flight","Count Assigned Tasks"
]

selected_operation = st.selectbox("Select Operation", operations)

if selected_operation.startswith("Create"):
    st.sidebar.header(selected_operation)
    if selected_operation.endswith("Airport"):
        airport_name = st.text_input("Airport Name")
        city = st.text_input("City")
        latitude = st.number_input("Latitude")
        longitude = st.number_input("Longitude")
        if st.button("Execute"):
            query = "INSERT INTO airport (airport_name, city, latitude, longitude) VALUES (%s, %s, %s, %s)"
            values = (airport_name, city, latitude, longitude)

            try:
                execute_query(query, values)
                st.success("Airport data inserted successfully!")
            except Exception as e:
                st.error(f"Error inserting data: {e}")

    elif selected_operation.endswith("Employee"):
        st.sidebar.header(selected_operation)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        is_admin = st.checkbox("Is Admin")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phno = st.text_input("Phone Number")
        role = st.text_input("Role")

        if st.button("Execute"):
            if selected_operation.startswith("Create"):
                query = "INSERT INTO employee (username, password, is_admin, name, email, phno, role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (username, password, is_admin, name, email, phno, role)

                try:
                    execute_query(query, values)
                    st.success("Employee data created successfully!")
                except Exception as e:
                    st.error(f"Error creating employee data: {e}")


    elif selected_operation.endswith("Task"):
        st.sidebar.header(selected_operation)
        descrip = st.text_area("Description")
        deadline = st.date_input("Deadline")
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        roles_req = st.text_input("Roles Required")

        if st.button("Execute"):
            if selected_operation.startswith("Create"):
                query = "INSERT INTO task (descrip, deadline, status, roles_req) VALUES (%s, %s, %s, %s)"
                values = (descrip, deadline, status, roles_req)

                try:
                    execute_query(query, values)
                    st.success("Task data created successfully!")
                except Exception as e:
                    st.error(f"Error creating task data: {e}")

    elif selected_operation.endswith("Flight"):
        st.sidebar.header(selected_operation)
        flight_no = st.text_input("Flight Number")
        departure_city = st.text_input("Departure City")
        arrival_city = st.text_input("Arrival City")
        departure_time = st.datetime_input("Departure Time")
        arrival_time = st.datetime_input("Arrival Time")
        aircraft_model = st.text_input("Aircraft Model")

        if st.button("Execute"):
            if selected_operation.startswith("Create"):
                query = "INSERT INTO flight (flight_no, departure_city, arrival_city, depature_time, arrival_time, aircraft_model) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (flight_no, departure_city, arrival_city, departure_time, arrival_time, aircraft_model)

                try:
                    execute_query(query, values)
                    st.success("Flight data created successfully!")
                except Exception as e:
                    st.error(f"Error creating flight data: {e}")

elif selected_operation.startswith("Read"):
    st.sidebar.header(selected_operation)

    if selected_operation.endswith("Airports"):
        if st.button("Execute"):
            query = "SELECT * FROM airport"
            airports = execute_query(query, fetchone=False)
            st.write("Airports:")
            st.write(pd.DataFrame(airports, columns=["Airport ID", "Airport Name", "City", "Latitude", "Longitude"]))

    elif selected_operation.endswith("Employees"):
        if st.button("Execute"):
            query = "SELECT * FROM employee"
            employees = execute_query(query, fetchone=False)

            columns = [i[0] for i in execute_query("SHOW columns FROM employee", fetchone=False)]

            st.write("Employees:")
            st.write(pd.DataFrame(employees, columns=columns))
            


    elif selected_operation.endswith("Tasks"):
        if st.button("Execute"):
            query = "SELECT * FROM task"
            tasks = execute_query(query, fetchone=False)
            st.write("Tasks:")
            st.write(pd.DataFrame(tasks, columns=["Task ID", "Description", "Deadline", "Status", "Roles Required"]))

    elif selected_operation.endswith("Flights"):
        if st.button("Execute"):
            query = "SELECT * FROM flight"
            flights = execute_query(query, fetchone=False)
            st.write("Flights:")
            st.write(pd.DataFrame(flights, columns=["Flight ID", "Flight Number", "Departure City", "Arrival City", "Departure Time", "Arrival Time", "Aircraft Model"]))

elif selected_operation.startswith("Update"):
    st.sidebar.header(selected_operation)

    if selected_operation.endswith("Airport"):
        airport_id = st.number_input("Enter Airport ID for Update")
        airport_name = st.text_input("Airport Name")
        city = st.text_input("City")
        latitude = st.number_input("Latitude")
        longitude = st.number_input("Longitude")

        if st.button("Execute"):
            query = "UPDATE airport SET airport_name=%s, city=%s, latitude=%s, longitude=%s WHERE airport_id=%s"
            values = (airport_name, city, latitude, longitude, airport_id)

            try:
                execute_query(query, values)
                st.success("Airport data updated successfully!")
            except Exception as e:
                st.error(f"Error updating airport data: {e}")


    elif selected_operation.endswith("Employee"):
        st.sidebar.header(selected_operation)
        employee_id = st.number_input("Enter Employee ID for Update")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        is_admin = st.checkbox("Is Admin")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phno = st.text_input("Phone Number")
        role = st.text_input("Role")

        if st.button("Execute"):
            query = "UPDATE employee SET username=%s, password=%s, is_admin=%s, name=%s, email=%s, phno=%s, role=%s WHERE emp_id=%s"
            values = (username, password, is_admin, name, email, phno, role, employee_id)

            try:
                execute_query(query, values)
                st.success("Employee data updated successfully!")
            except Exception as e:
                st.error(f"Error updating employee data: {e}")


    elif selected_operation.endswith("Task"):
        st.sidebar.header(selected_operation)
        task_id = st.number_input("Enter Task ID for Update")
        descrip = st.text_area("Description")
        deadline = st.date_input("Deadline")
        status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])
        roles_req = st.text_input("Roles Required")

        if st.button("Execute"):
            query = "UPDATE task SET descrip=%s, deadline=%s, status=%s, roles_req=%s WHERE task_id=%s"
            values = (descrip, deadline, status, roles_req, task_id)

            try:
                execute_query(query, values)
                st.success("Task data updated successfully!")
            except Exception as e:
                st.error(f"Error updating task data: {e}")


    elif selected_operation.endswith("Flight"):
        st.sidebar.header(selected_operation)
        flight_id = st.number_input("Enter Flight ID for Update")
        flight_no = st.text_input("Flight Number")
        departure_city = st.text_input("Departure City")
        arrival_city = st.text_input("Arrival City")
        departure_time = st.datetime_input("Departure Time")
        arrival_time = st.datetime_input("Arrival Time")
        aircraft_model = st.text_input("Aircraft Model")

        if st.button("Execute"):
            query = "UPDATE flight SET flight_no=%s, departure_city=%s, arrival_city=%s, depature_time=%s, arrival_time=%s, aircraft_model=%s WHERE flight_id=%s"
            values = (flight_no, departure_city, arrival_city, departure_time, arrival_time, aircraft_model, flight_id)

            try:
                execute_query(query, values)
                st.success("Flight data updated successfully!")
            except Exception as e:
                st.error(f"Error updating flight data: {e}")

elif selected_operation.startswith("Delete"):
    st.sidebar.header(selected_operation)

    if selected_operation.endswith("Airport"):
        airport_id_delete = st.number_input("Enter Airport ID for Delete")
        if st.button("Execute"):
            query = "DELETE FROM airport WHERE airport_id=%s"
            values = (airport_id_delete,)

            try:
                execute_query(query, values)
                st.success("Airport data deleted successfully!")
            except Exception as e:
                st.error(f"Error deleting airport data: {e}")

    elif selected_operation.endswith("Employee"):
        employee_id_delete = st.number_input("Enter Employee ID for Delete")
        if st.button("Execute"):
            query = "DELETE FROM employee WHERE emp_id=%s"
            values = (employee_id_delete,)

            try:
                execute_query(query, values)
                st.success("Employee data deleted successfully!")
            except Exception as e:
                st.error(f"Error deleting employee data: {e}")

    elif selected_operation.endswith("Task"):
        task_id_delete = st.number_input("Enter Task ID for Delete")
        if st.button("Execute"):
            query = "DELETE FROM task WHERE task_id=%s"
            values = (task_id_delete,)

            try:
                execute_query(query, values)
                st.success("Task data deleted successfully!")
            except Exception as e:
                st.error(f"Error deleting task data: {e}")

    elif selected_operation.endswith("Flight"):
        flight_id_delete = st.number_input("Enter Flight ID for Delete")
        if st.button("Execute"):
            query = "DELETE FROM flight WHERE flight_id=%s"
            values = (flight_id_delete,)

            try:
                execute_query(query, values)
                st.success("Flight data deleted successfully!")
            except Exception as e:
                st.error(f"Error deleting flight data: {e}")

elif selected_operation == "Count Assigned Tasks":
    st.sidebar.header(selected_operation)
    
    # Add an input field for employee ID
    employee_id = st.number_input("Employee ID")

    # Call the function to get assigned tasks count
    assigned_tasks_count = count_assigned_tasks(employee_id)
    st.write(f"Number of Assignments: {assigned_tasks_count}")

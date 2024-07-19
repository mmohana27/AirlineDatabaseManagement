import streamlit as st
import pandas as pd
import mysql.connector
import folium
from streamlit_folium import folium_static

def execute_query(query):
    connection = mysql.connector.connect(
        host="name",
        user="name",
        password="abc",
        database="AIRLINEDBMS"
    )

    cursor = connection.cursor()
    cursor.execute(query) 

    if query.strip().upper().startswith("SELECT"):
        result = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        cursor.close()
        connection.close()
        return result, column_names

    connection.commit()
    cursor.close()
    connection.close()
    return None, None


def employee_page():

    st.title("Employee View Page")

    employee_id = st.number_input("Enter Your Employee ID:", min_value=1)

    if st.button("Execute"):

        query_assigned_tasks = f"SELECT Task.* FROM Task " \
                               f"JOIN Employee_Task_Assignment ON Task.task_id = Employee_Task_Assignment.task_id " \
                               f"WHERE Employee_Task_Assignment.emp_id = {employee_id}"
        result_assigned_tasks, column_names_assigned_tasks = execute_query(query_assigned_tasks)

        st.header("Your Assigned Tasks")
        if result_assigned_tasks:
            st.table(pd.DataFrame(result_assigned_tasks, columns=column_names_assigned_tasks))
        else:
            st.info("No tasks assigned to you.")

        query_assigned_flights = f"SELECT Flight.* FROM Flight " \
                                 f"JOIN Employee_Flight_Assignment ON Flight.flight_id = Employee_Flight_Assignment.flight_id " \
                                 f"WHERE Employee_Flight_Assignment.emp_id = {employee_id}"
        result_assigned_flights, column_names_assigned_flights = execute_query(query_assigned_flights)

        st.header("Flights Assigned to You")
        if result_assigned_flights:
            st.table(pd.DataFrame(result_assigned_flights, columns=column_names_assigned_flights))
        else:
            st.info("No flights assigned to you.")

        query_personal_tasks = f"SELECT * FROM Task WHERE roles_req = 'employee' AND task_id NOT IN " \
                               f"(SELECT task_id FROM Employee_Task_Assignment WHERE emp_id = {employee_id})"
        result_personal_tasks, column_names_personal_tasks = execute_query(query_personal_tasks)

        st.header("Your Personal Tasks")
        if result_personal_tasks:
            st.table(pd.DataFrame(result_personal_tasks, columns=column_names_personal_tasks))
        else:
            st.info("No personal tasks available.")
        
        query_airports = "SELECT * FROM airport"
        result_airports, column_names_airports = execute_query(query_airports)

        st.header("All Airports on Map")
        if result_airports:
            m = folium.Map(location=[result_airports[0][3], result_airports[0][4]], zoom_start=10, control_scale=True)

            for airport in result_airports:
                folium.Marker(location=[airport[3], airport[4]], popup=airport[1]).add_to(m)

            folium_static(m, width=1000, height=600) 
        else:
            st.info("No airports available.")

def task_updation_page():
    st.title("Task Updation Page")

    task_id = st.number_input("Enter Task ID to Update:", min_value=1)
    new_status = st.selectbox("Select New Status:", ["In Progress", "Completed", "Pending"])

    if st.button("Update Task Status"):
        # Write the code to update the task status in the database
        update_query = f"UPDATE Task SET status = '{new_status}' WHERE task_id = {task_id}"
        execute_query(update_query)
        st.success("Task status updated successfully!")

if __name__ == "__main__":
    st.set_page_config(page_title="Employee Airline Page", page_icon="✈️")
    page = st.sidebar.selectbox("Select Page", ["Employee View Page", "Task Updation Page"])

    if page == "Employee View Page":
        employee_page()
    elif page == "Task Updation Page":
        task_updation_page()
    
    #Sidebar
    st.sidebar.title("Employee Table")
    query_employee_table = "SELECT * FROM employee"
    result_employee_table, column_names_employee_table = execute_query(query_employee_table)

    if result_employee_table:
        st.sidebar.table(pd.DataFrame(result_employee_table, columns=column_names_employee_table))
    else:
        st.sidebar.info("No employee data available.")

    
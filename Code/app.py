# Importing pakages
import streamlit as st
import mysql.connector

from create import create
from database import create_table
from delete import delete
from read import read
from update import update
from datetime import date, timedelta
from query import query
from read_bookings import read_bookings
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()
#
# c.execute("CREATE DATABASE ebike")


def main():
    st.title("tourismmanagementsystem")
    menu = ["Add packages", "View packages", "Edit packages", "Remove packages","View bookings","Query"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Add packages":
        st.subheader("Enter package Details:")
        create()

    elif choice == "View packages":
        st.subheader("View created tasks")
        read()

    elif choice == "Edit packages":
        st.subheader("Update created tasks")
        update()

    elif choice == "Remove packages":
        st.subheader("Delete created tasks")
        delete()
    
    elif choice == "View bookings":
        st.subheader("Bookings")
        read_bookings()

    elif choice == "Query":
        st.subheader("Query")
        query()
    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
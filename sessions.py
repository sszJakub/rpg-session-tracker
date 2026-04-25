import mysql.connector
from mysql.connector import Error
from credentials import my_host, my_user, my_password, my_database
from db import connection


def add_session():
    cursor = connection.cursor()
    date = input("What is the date of the session? ")
    notes = input("Any notes for the session? ")
    cursor.execute("INSERT INTO sessions (date, notes) VALUES (%s, %s)", (date, notes))
    connection.commit()
    print("Session has been added.")

def display_all_sessions():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sessions")
    print("----------------------------")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Date: {row[1]} | Notes: {row[2]}")
    print("----------------------------\n")

def delete_session():
    cursor = connection.cursor()
    while True:
        session_id = input("Which session id do you want to delete? ")
        if not session_id.isdigit():
            print("Invalid id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM sessions WHERE id = %s", (session_id,))
        
        if cursor.fetchone() is None:
            print("Session does not exist\n")
            continue
        break
    cursor.execute("DELETE FROM sessions WHERE id = %s", (session_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Session has been deleted.")
    else:
        print("No session found with the given id.")
    print()

def update_session():
    cursor = connection.cursor()
    while True:
        session_id = input("Which session id do you want to update? ")
        if not session_id.isdigit():
            print("Invalid id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM sessions WHERE id = %s", (session_id,))
        if cursor.fetchone() is None:
            print("Session does not exist\n")
            continue
        break
    new_date = input("What should be the new date of the session? ")
    new_notes = input("What should be the new notes for the session? ")
    cursor.execute("UPDATE sessions SET date = %s, notes = %s WHERE id = %s", (new_date, new_notes, session_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Session has been updated.")
    else:
        print("Session not found with the given id.")
    print()

def manage_sessions():
    while True:
        print("1. Add session")
        print("2. Display sessions")
        print("3. Delete session")
        print("4. Update session")
        print("5. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_session()
        elif choice == "2":
            display_all_sessions()
        elif choice == "3":
            delete_session()
        elif choice == "4":
            update_session()
        elif choice == "5":
            break
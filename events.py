import mysql.connector
from mysql.connector import Error
from credentials import my_host, my_user, my_password, my_database
from db import connection, cursor


def add_event():
    session_id = input("What is the session id? ")
    description = input("What is the description of the event? ")
    cursor.execute("INSERT INTO events (session_id, description) VALUES (%s, %s)", (session_id, description))
    connection.commit()
    print("Event has been added.")

def display_all_events():
    cursor.execute("SELECT * FROM events")
    print("----------------------------")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Session ID: {row[1]} | Description: {row[2]}")
    print("----------------------------\n")

def show_events_for_session():
    session_id = input("Enter session ID: ")
    cursor.execute("SELECT * FROM events WHERE session_id = %s", (session_id,))
    print("----------------------------")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Session ID: {row[1]} | Description: {row[2]}")
    print("----------------------------\n")

def delete_event():
    event_id = input("Which event id do you want to delete? ")
    if not event_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Event has been deleted.")
    else:
        print("No event found with the given id.")
    print()

def update_event():
    event_id = input("Which event id do you want to update? ")
    if not event_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    new_description = input("What should be the new description for the event? ")
    cursor.execute("UPDATE events SET description = %s WHERE id = %s", (new_description, event_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Event has been updated.")
    else:
        print("Event not found with the given id.")
    print()

def manage_events():
    while True:
        print("1. Add event")
        print("2. Display all events")
        print("3. Show events for a session")
        print("4. Delete event")
        print("5. Update event")
        print("6. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            display_all_events()
        elif choice == "3":
            show_events_for_session()
        elif choice == "4":
            delete_event()
        elif choice == "5":
            update_event()
        elif choice == "6":
            break
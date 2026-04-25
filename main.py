import mysql.connector
from mysql.connector import Error
from credentials import my_host, my_user, my_password, my_database
from events import *
from sessions import *
from players import *
from characters import *
from db import connection, cursor


def exit_program():
    print("Exiting the program.")
    connection.close()
    exit()

def main():
    print("Welcome to the RPG database management system!")
    print("You can manage players and characters in the database.")
    while True:
        print("Which table do you want to manage?")
        print("1. Players")
        print("2. Characters")
        print("3. Events")
        print("4. Sessions")
        print("5. Exit")

        table_choice = input("Choose an option: ")
        if table_choice == "1":
            manage_players()
        elif table_choice == "2":
            manage_characters()
        elif table_choice == "3":
            manage_events()
        elif table_choice == "4":
            manage_sessions()
        elif table_choice == "5":
            exit_program()


main()


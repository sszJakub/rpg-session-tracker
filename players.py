import mysql.connector
from mysql.connector import Error
from credentials import my_host, my_user, my_password, my_database
from db import connection, cursor


def add_player():
    name = input("What is the player's name? ")
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    connection.commit()
    print("Player has been added.")

def display_all_players():
    cursor.execute("SELECT * FROM players") 
    for row in cursor.fetchall():
        print("----------------------------")
        print(f"ID: {row[0]} | Name: {row[1]}")
        print("----------------------------\n")
    print()

def delete_player():
    player_id = input("Which player id do you want to delete? ")
    if not player_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    cursor.execute("DELETE FROM players WHERE id = %s", (player_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Player has been deleted.")
    else:
        print("No player found with the given id.")
    print()

def update_player():
    player_id = input("Which player id do you want to update? ")
    if not player_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    new_name = input("What should be the new name of the player? ")
    cursor.execute("UPDATE players SET name = %s WHERE id = %s", (new_name, player_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Player has been updated.")
    else:
        print("Player not found with the given id.")
    print()

def manage_players():
    while True:
        print("1. Add player")
        print("2. Display players")
        print("3. Delete player")
        print("4. Update player")
        print("5. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            display_all_players()
        elif choice == "3":
            delete_player()
        elif choice == "4":
            update_player()
        elif choice == "5":
            break
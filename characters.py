import mysql.connector
from mysql.connector import Error
from credentials import my_host, my_user, my_password, my_database
from db import connection


def add_character_to_db(name, race, character_class, player_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO characters (name, race, character_class, player_id) VALUES (%s, %s, %s, %s)", (name, race, character_class, player_id))
    connection.commit()
    print("Character has been added.")


def add_character():
    cursor = connection.cursor()
    name = input("What is the character's name? ")
    race = input("What is the character's race? ")
    character_class = input("What is the character's class? ")
    while True:
        player_id = input("Which player id does the character belong to? ")
        if not player_id.isdigit():
            print("Invalid player id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM players WHERE id = %s", (player_id,))
        if cursor.fetchone() is None:
            print("Player does not exist.")
            continue
        break
    add_character_to_db(name, race, character_class, player_id)
    print()


def display_all_characters():
    cursor = connection.cursor()
    cursor.execute("""
        SELECT characters.id, characters.name, characters.race, characters.character_class, players.name
        FROM characters
        JOIN players ON characters.player_id = players.id
    """)
    print("----------------------------")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Race: {row[2]} | Class: {row[3]} | Player: {row[4]}")
    print("----------------------------\n")


def show_character_details():
    cursor = connection.cursor()
    while True:
        character_id = input("Enter character ID: ")
        if not character_id.isdigit():
            print("Invalid ID\n")
            continue
        cursor.execute("SELECT id FROM characters WHERE id = %s", (character_id,))
        if cursor.fetchone() is None:
            print("Character does not exist\n")
            continue
        break
    cursor.execute("""
        SELECT characters.id, characters.name, characters.race, characters.character_class, players.name
        FROM characters
        JOIN players ON characters.player_id = players.id
        WHERE characters.id = %s
    """, (character_id,))
    row = cursor.fetchone()
    if row is None:
        print("Character not found\n")
        return
    print("----------------------------")
    print("\nCharacter details:")
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Race: {row[2]}")
    print(f"Class: {row[3]}")
    print(f"Player: {row[4]}")
    print("----------------------------\n")


def delete_character_from_db(character_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM characters WHERE id = %s", (character_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Character has been deleted.")
    else:
        print("No character found with the given id.")
    print()



def delete_character():
    cursor = connection.cursor()
    while True:
        character_id = input("Which character id do you want to delete? ")
        if not character_id.isdigit():
            print("Invalid id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM characters WHERE id = %s", (character_id,))
        if cursor.fetchone() is None:
            print("Character does not exist")
            continue
        break
    delete_character_from_db(character_id)
    print()



def update_character_in_db(character_id, new_name, new_race, new_class, new_player_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE characters SET name = %s, race = %s, character_class = %s, player_id = %s WHERE id = %s", (new_name, new_race, new_class, new_player_id, character_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Character has been updated.")
    else:
        print("Character not found with the given id.")

def update_character():
    cursor = connection.cursor()
    while True:
        character_id = input("Which character id do you want to update? ")
        if not character_id.isdigit():
            print("Invalid id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM characters WHERE id = %s", (character_id,))
        if cursor.fetchone() is None:
            print("Character does not exist")
            continue
        break
    new_name = input("What should be the new name of the character? ")
    new_race = input("What should be the new race of the character? ")
    new_class = input("What should be the new class of the character? ")
    new_player_id = input("Which player id does the character belong to? ")
    while True:
        if not new_player_id.isdigit():
            print("Invalid player id. Please enter a number.")
            continue
        cursor.execute("SELECT id FROM players WHERE id = %s", (new_player_id,))
        if cursor.fetchone() is None:
            print("Player does not exist.")
            continue
        break
    update_character_in_db(character_id, new_name, new_race, new_class, new_player_id)
    print()


def manage_characters():
    while True:
        print("1. Add character")
        print("2. Display character details")
        print("3. Display all characters")
        print("4. Delete character")
        print("5. Update character")
        print("6. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            add_character()
        elif choice == "2":
            show_character_details()
        elif choice == "3":
            display_all_characters()
        elif choice == "4":
            delete_character()
        elif choice == "5":
            update_character()
        elif choice == "6":
            break
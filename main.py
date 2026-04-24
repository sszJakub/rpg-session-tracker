import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(
    host = "localhost",
    user = "kubas",
    password = "haslo123",
    database = "rpg_db"
)

cursor = connection.cursor()


def add_player():
    name = input("What is the player's name? ")
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    connection.commit()
    print("Player has been added.")

def display_all_players():
    cursor.execute("SELECT * FROM players") 
    for row in cursor.fetchall():
        print(row)
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
    print("1. Add player")
    print("2. Display players")
    print("3. Delete player")
    print("4. Update player")
    print("5. Exit")

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
        exit_program()



def add_character():
    name = input("What is the character's name?")
    race = input("What is the character's race?")
    class_ = input("What is the character's class? ")
    player_id = input("Which player id does the character belong to? ")
    if not player_id.isdigit():
        print("Invalid player id. Please enter a number.")
        return
    cursor.execute("INSERT INTO characters (name, race, class, player_id) VALUES (%s, %s, %s, %s)", (name, race, class_, player_id))
    connection.commit()
    print("Character has been added.")
    print()


def display_all_characters():
    cursor.execute("SELECTO * FROM characters")
    for row in cursor.fetchall():
        print(row)
    print()



def delete_character():
    character_id = input("Which character id do you want to delete?")
    if not character_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    cursor.execute("DELETE FROM characters WHERE id = %s", (character_id,))
    connection.commit()
    if cursor.rowcount > 0:        
        print("Character has been deleted.")
    else:        
        print("No character found with the given id.")
    print()


def update_character():
    character_id = input("Which character id do you want to update?")
    if not character_id.isdigit():
        print("Invalid id. Please enter a number.")
        return
    new_name = input("What should be the new name of the character? ")
    new_race = input("What should be the new race of the character? ")
    new_class = input("What should be the new class of the character? ")
    cursor.execute("UPDATE characters SET name = %s, race = %s, class = %s WHERE id = %s", (new_name, new_race, new_class, character_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Character has been updated.")
    else:
        print("Character not found with the given id.")
    print()


def manage_characters():
    print("1. Add character")
    print("2. Display characters")
    print("3. Delete character")
    print("4. Update character")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_character()
    elif choice == "2":
        display_all_characters()
    elif choice == "3":
        delete_character()
    elif choice == "4":
        update_character()
    elif choice == "5":
        exit_program()


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
        print("3. Exit")

        table_choice = input("Choose an option: ")
        if table_choice == "1":
            manage_players()
        elif table_choice == "2":
            manage_characters()
        elif table_choice == "3":
            exit_program()





main()












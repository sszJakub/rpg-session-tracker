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
    name = input("Jak nazywa się gracz? ")
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    connection.commit()

def display_all_players():
    cursor.execute("SELECT * FROM players") 
    for row in cursor.fetchall():
        print(row)

def delete_player():
    player_id = input("Jakie id gracza chcesz usunąć? ")
    cursor.execute("DELETE FROM players WHERE id = %s", (player_id,))
    connection.commit()

def update_player():
    player_id = input("Jakie id gracza chcesz zaktualizować? ")
    new_name = input("Jak ma nazywać się gracz? ")
    cursor.execute("UPDATE players SET name = %s WHERE id = %s", (new_name, player_id))
    connection.commit()






def main():
    while True:
        print("1. Dodaj gracza")
        print("2. Wyświetl graczy")
        print("3. Usuń gracza")
        print("4. Zaktualizuj gracza")
        print("5. Wyjdź")

        choice = input("wybierz opcję: ")

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
    connection.close()





main()












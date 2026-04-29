import pytest
from players import *
from characters import *
import time


# Positive test cases
def test_add_character_to_db():
    try:
        character_name = f"Test_Character_to_add_{int(time.time())}"
        race = f"Test_Race_{int(time.time())}"
        character_class = f"Test_Class_{int(time.time())}"
        name = f"Test_Player_for_Character__{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        player_id = result[0]
        add_character_to_db(character_name, race, character_class, player_id)
        cursor.execute("SELECT id, name, race, character_class, player_id FROM characters WHERE name = %s AND race = %s AND character_class = %s AND player_id = %s", (character_name, race, character_class, player_id))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == character_name
        assert result[2] == race
        assert result[3] == character_class
        assert result[4] == player_id
        character_id = result[0]
    finally:
        delete_character_from_db(character_id)
        delete_player_from_db(player_id)



def test_delete_character_from_db():
    try:
        character_name = f"Test_Character_to_delete_{int(time.time())}"
        race = f"Test_Race_{int(time.time())}"
        character_class = f"Test_Class_{int(time.time())}"
        name = f"Test_Player_for_Character_{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        player_id = result[0]
        add_character_to_db(character_name, race, character_class, player_id)
        cursor.execute("SELECT id FROM characters WHERE name = %s AND race = %s AND character_class = %s AND player_id = %s", (character_name, race, character_class, player_id))
        result = cursor.fetchone()
        character_id = result[0]
    finally:
        delete_character_from_db(character_id)
        cursor.execute("SELECT id FROM characters WHERE id = %s", (character_id,))
        result = cursor.fetchone()
        assert result is None
        delete_player_from_db(player_id)


def test_update_character_in_db():
    try:
        character_name = f"Test_character_to_update_{int(time.time())}"
        race = f"Test_Race_to_update{int(time.time())}"
        character_class = f"Test_Class_to_update{int(time.time())}"
        name = f"Test_Player_for_Character_to_update_{int(time.time())}"
        name2 = f"Updated_Test_Player_{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        player_id = result[0]
        add_player_to_db(name2)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (name2,))
        result = cursor.fetchone()
        player_id2 = result[0]
        add_character_to_db(character_name, race, character_class, player_id)
        cursor.execute("SELECT id FROM characters WHERE name = %s AND race = %s AND character_class = %s AND player_id = %s", (character_name, race, character_class, player_id))
        result = cursor.fetchone()
        character_id = result[0]
        new_character_name = f"Updated_Character_to_update{int(time.time())}"
        new_race = f"Updated_race_{int(time.time())}"
        new_character_class = f"Updated_Class_{int(time.time())}"
        update_character_in_db(character_id, new_character_name, new_race, new_character_class, player_id2)
        cursor.execute("SELECT id, name, race, character_class, player_id FROM characters WHERE id = %s", (character_id,))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == new_character_name
        assert result[2] == new_race
        assert result[3] == new_character_class
        assert result[4] == player_id2
    finally:
        delete_character_from_db(character_id)
        delete_player_from_db(player_id)
        delete_player_from_db(player_id2)



# Negative test cases
def test_add_character_to_db_empty_fields():
    with pytest.raises(ValueError):
        add_character_to_db("", "", "", "")

def test_add_character_to_db_none_name():
    player_id = None
    try:
        test_player_name = f"Test_Player_for_Character_{int(time.time())}"
        add_player_to_db(test_player_name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (test_player_name,))
        result = cursor.fetchone()
        player_id = result[0]
        character_name = None
        race = f"Test_Race_{int(time.time())}"
        character_class = f"Test_Class_{int(time.time())}"
        cursor = connection.cursor(buffered=True)
        with pytest.raises(ValueError):
            add_character_to_db(character_name, race, character_class, player_id)
    finally:
        delete_player_from_db(player_id)

def test_add_character_to_db_none_race():
    player_id = None
    try:
        test_player_name = f"Test_Player_for_Character_{int(time.time())}"
        add_player_to_db(test_player_name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (test_player_name,))
        result = cursor.fetchone()
        player_id = result[0]
        character_name = f"Test_Character_to_add_{int(time.time())}"
        race = None
        character_class = f"Test_Class_{int(time.time())}"
        cursor = connection.cursor(buffered=True)
        with pytest.raises(ValueError):
            add_character_to_db(character_name, race, character_class, player_id)
    finally:
        delete_player_from_db(player_id)

def test_add_character_to_db_none_character_class():
    player_id = None
    try:
        test_player_name = f"Test_Player_for_Character_{int(time.time())}"
        add_player_to_db(test_player_name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM players WHERE name = %s", (test_player_name,))
        result = cursor.fetchone()
        player_id = result[0]
        character_name = f"Test_Character_to_add_{int(time.time())}"
        race = f"Test_Race_{int(time.time())}"
        character_class = None
        cursor = connection.cursor(buffered=True)
        with pytest.raises(ValueError):
            add_character_to_db(character_name, race, character_class, player_id)
    finally:
        delete_player_from_db(player_id)

def test_add_character_to_db_none_player_id():
    player_id = None
    character_name = f"Test_Character_to_add_{int(time.time())}"
    race = f"Test_Race_{int(time.time())}"
    character_class = f"Test_Class_{int(time.time())}"
    with pytest.raises(ValueError):
        add_character_to_db(character_name, race, character_class, player_id)







def test_delete_character_from_db_invalid_id():
    with pytest.raises(ValueError):
        delete_character_from_db("")


def test_update_character_in_db_invalid_id():
    with pytest.raises(ValueError):
        update_character_in_db("", "", "", "", "")









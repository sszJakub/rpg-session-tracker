import pytest
from players import *
import time

# Positive test cases 
def test_add_player_to_db():
    try:
        name = f"Test_Player_{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id, name FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == name
    finally:
        delete_player_from_db(result[0])


def test_delete_player_from_db():
    try:
        name = f"Test_Player_To_Delete_{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id, name FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        player_id = result[0]
        cursor.fetchall()
    finally:
        delete_player_from_db(player_id)
        cursor.execute("SELECT id FROM players WHERE id = %s", (player_id,))
        result = cursor.fetchone()
        cursor.fetchall()
        assert result is None


def test_update_player_in_db():
    player_id = None
    try: 
        name = f"Test_Player_to_Update_{int(time.time())}"
        add_player_to_db(name)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id, name FROM players WHERE name = %s", (name,))
        result = cursor.fetchone()
        player_id = result[0]
        new_name = f"Updated_{name}"
        update_player_in_db(player_id, new_name)
        cursor.execute("SELECT id, name FROM players WHERE id = %s", (player_id,))
        result = cursor.fetchone()
        assert result is not None
        assert result[1] == new_name
    finally:
        if player_id:
            delete_player_from_db(player_id)


# Negative test cases
def test_add_player_to_db_empty_name():
    with pytest.raises(ValueError):
        add_player_to_db("")

def test_delete_player_from_db_nonexistent():
    non_existent_id = 999999
    delete_player_from_db(non_existent_id)
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id FROM players WHERE id = %s", (non_existent_id,))
    result = cursor.fetchone()
    assert result is None


def test_update_player_in_db_nonexistent():
    non_existent_id = 999999
    new_name = "Should_Not_Update"
    update_player_in_db(non_existent_id, new_name)
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id FROM players WHERE id = %s", (non_existent_id,))
    result = cursor.fetchone()
    assert result is None

































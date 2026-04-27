import pytest
from players import *
import time


def test_add_player_to_db():
    name = f"Test_Player_{int(time.time())}"
    add_player_to_db(name)
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id, name FROM players WHERE name = %s", (name,))
    result = cursor.fetchone()
    assert result is not None
    assert result[1] == name
    delete_player_from_db(result[0])


def test_delete_player_from_db():
    name = f"Test_Player_To_Delete_{int(time.time())}"
    add_player_to_db(name)
    cursor = connection.cursor(buffered=True)
    cursor.execute("SELECT id, name FROM players WHERE name = %s", (name,))
    result = cursor.fetchone()
    player_id = result[0]
    cursor.fetchall()
    delete_player_from_db(player_id)
    cursor.execute("SELECT id FROM players WHERE id = %s", (player_id,))
    result = cursor.fetchone()
    cursor.fetchall()
    assert result is None


def test_update_player_in_db():
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
    delete_player_from_db(player_id)





































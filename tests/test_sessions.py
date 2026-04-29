import pytest
from sessions import *
import time

# Posiitive test cases
def test_add_session_to_db():
    try:
        test_date = "2000-01-01"
        test_notes = f"Test_Notes_{int(time.time())}"
        add_session_to_db(test_date, test_notes)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", (test_date, test_notes))
        result = cursor.fetchone()
        assert result is not None
    except Exception as e:
        pytest.fail(f"Error occurred while testing add_session_to_db: {e}")
    finally:
        if result:
            delete_session_from_db(result[0])


def test_delete_session_from_db():
    try:
        test_date = "2001-01-01"
        test_notes = f"Test_notes_to_delete_{int(time.time())}"
        add_session_to_db(test_date, test_notes)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", (test_date, test_notes))
        result = cursor.fetchone()
        session_id = result[0]
        cursor.fetchall()
    finally:
        delete_session_from_db(session_id)
        cursor.execute("SELECT id FROM sessions WHERE id = %s", (session_id,))
        result_to_delete = cursor.fetchone()
        cursor.fetchall()
        assert result_to_delete is None


def test_update_session_in_db():
    session_id = None
    try:
        test_date = "2002-01-01"
        test_notes = f"Test_notes_to_update_{int(time.time())}"
        add_session_to_db(test_date, test_notes)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", (test_date, test_notes))
        result = cursor.fetchone()
        session_id = result[0]
        cursor.fetchall()
        new_date = "2003-01-01"
        new_notes = f"Updated_notes_{int(time.time())}"
        update_session_in_db(session_id, new_date, new_notes)
    except Exception as e:
        pytest.fail(f"Error occurred while testing update_session_in_db: {e}")
    finally:
        if session_id:
            delete_session_from_db(session_id)


# Negative test cases
def test_add_session_to_db_empty_fields():
    with pytest.raises(ValueError):
        add_session_to_db("", "")
    
def test_add_session_to_db_invalid_date_format():
    with pytest.raises(ValueError):
        add_session_to_db("invalid-date", "Test notes")

def test_add_session_to_db_empty_notes():
    with pytest.raises(ValueError):
        add_session_to_db("2000-01-01", "")
    
def test_delete_session_from_db_empty_id():
    with pytest.raises(ValueError):
        delete_session_from_db("")












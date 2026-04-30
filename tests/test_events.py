import pytest
from events import *
import time
from sessions import *

# Positive test cases
def test_add_event_to_db():
    try:
        test_description = f"Test_Description_{int(time.time())}"
        add_session_to_db("2000-01-01", "Test session for events")
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", ("2000-01-01", "Test session for events"))
        session_id = cursor.fetchone()[0]
        add_event_to_db(session_id, test_description)
        cursor.execute("SELECT id FROM events WHERE session_id = %s AND description = %s", (session_id, test_description))
        result = cursor.fetchone()
        assert result is not None
    except Exception as e:
        pytest.fail(f"Error occurred while testing add_event_to_db: {e}")
    finally:
        if result:
            delete_event_from_db(result[0])
        delete_session_from_db(session_id)

def test_delete_event_from_db():
    try:
        test_description = f"Test_description_to_delete_{int(time.time())}"
        test_session_date = "2001-01-01"
        test_session_notes = "Test session for deleting events"
        add_session_to_db(test_session_date, test_session_notes)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", (test_session_date, test_session_notes))
        session_id = cursor.fetchone()[0]
        add_event_to_db(session_id, test_description)
        cursor.execute("SELECT id FROM events WHERE session_id = %s AND description = %s", (session_id, test_description))
        event_id = cursor.fetchone()[0]
    finally:
        if event_id:
            delete_event_from_db(event_id)
            cursor.execute("SELECT id FROM events WHERE id = %s", (event_id,))
            result_to_delete = cursor.fetchone()
            assert result_to_delete is None
        delete_session_from_db(session_id)

def test_update_event_in_db():
    event_id = None
    session_id = None
    try:
        test_description = f"Test_description_to_update_{int(time.time())}"
        test_session_date = "2002-01-01"
        test_session_notes = "Test session for updating events"
        add_session_to_db(test_session_date, test_session_notes)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM sessions WHERE date = %s AND notes = %s", (test_session_date, test_session_notes))
        session_id = cursor.fetchone()[0]
        add_event_to_db(session_id, test_description)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT id FROM events WHERE session_id = %s AND description = %s", (session_id, test_description))
        event_id = cursor.fetchone()[0]
        new_description = f"Updated_Test_description_{int(time.time())}"
        update_event_in_db(event_id, new_description)
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT description FROM events WHERE id = %s", (event_id,))
        updated_description = cursor.fetchone()[0]
        assert updated_description == new_description
    except Exception as e:
        pytest.fail(f"Error occurred while testing update_event_in_db: {e}")
    finally:
        if event_id:
            delete_event_from_db(event_id)
        if session_id:
            delete_session_from_db(session_id)
        

























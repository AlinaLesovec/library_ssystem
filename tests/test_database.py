import pytest
from database.database_manager import DatabaseManager

def test_db_connection():
    db = DatabaseManager()
    assert db.connection is not None
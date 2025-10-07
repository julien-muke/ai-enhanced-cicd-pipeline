# test_app.py
import pytest
from app import add_numbers, get_user_greeting

def test_add_numbers_success():
    """Test successful addition of two integers."""
    assert add_numbers(5, 10) == 15

def test_add_numbers_floats():
    """Test successful addition of two floats."""
    assert add_numbers(2.5, 2.5) == 5.0

def test_add_numbers_type_error():
    """Test that add_numbers raises a TypeError for non-numeric input."""
    with pytest.raises(TypeError):
        add_numbers("a", 5)

def test_get_user_greeting_success():
    """Test a successful greeting with a valid user dictionary."""
    user = {"name": "Alex", "city": "Zürich"}
    assert get_user_greeting(user) == "Hello, Alex from Zürich!"

def test_get_user_greeting_missing_key():
    """Test the greeting when a key is missing from the user data."""
    user = {"name": "Alex"}
    assert get_user_greeting(user) == "Hello, Guest! User data is incomplete."

def test_get_user_greeting_invalid_data():
    """Test the greeting with invalid (non-dictionary) input."""
    assert get_user_greeting("not a dict") == "Hello, Guest! Invalid user data provided."

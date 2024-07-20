import pytest
from validations.auth_validation import validate_username, validate_password

def test_validate_username():
    assert validate_username("validuser")[0] == True
    assert validate_username("u")[0] == False
    assert validate_username("a"*256)[0] == False
    assert validate_username("invalid;user")[0] == False

def test_validate_password():
    assert validate_password("ValidPass123")[0] == True
    assert validate_password("short1A")[0] == False
    assert validate_password("nouppercase1")[0] == False
    assert validate_password("NOLOWERCASE1")[0] == False

import pytest
from config import Config

def test_load_config():
    config = Config('server.config.json')

    assert config.JWT_SECRET_KEY == 'your_jwt_secret_key'
    assert config.DATABASE_URI == 'postgresql://postgres:A12345aa@localhost:5432/Smartbox SQL'
    assert config.LOG_LEVEL == 'WARNING'

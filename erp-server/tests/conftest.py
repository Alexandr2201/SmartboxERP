import os
import pytest

from app import app as flask_app
from db.database import Base, Session, engine
from config import Config

@pytest.fixture(scope='session', autouse=True)
def set_test_config():
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
    yield
    os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope='module')
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture(scope='module')
def test_client():
    with flask_app.test_client() as client:
        yield client

@pytest.fixture(scope='module')
def init_database():
    Base.metadata.create_all(engine)
    yield Session()  # Возвращаем объект сессии для использования в тестах
    Base.metadata.drop_all(engine)

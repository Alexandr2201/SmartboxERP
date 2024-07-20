import pytest
import logging
from logger import auth_logger, setup_logger

def test_logger_setup():
    logger = setup_logger('test_logger', 'test.log', level=logging.DEBUG)
    assert logger.name == 'test_logger'
    assert logger.level == logging.DEBUG

def test_auth_logger():
    assert auth_logger.name == 'auth_service_logger'
    assert auth_logger.level == logging.WARNING

""" import json
import pytest
import uuid
from db.models import User

def test_login_success(test_client, init_database):
    user_uuid = uuid.uuid4()  # Генерируем UUID
    user = User(uuid=user_uuid, username='testuser', password='TestPass123')
    init_database.add(user)
    init_database.commit()

    login_data = {
        'username': 'testuser',
        'password': 'TestPass123'
    }

    response = test_client.post('/login', data=json.dumps(login_data), content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data

def test_login_failure(test_client, init_database):
    login_data = {
        'username': 'wronguser',
        'password': 'WrongPass123'
    }

    response = test_client.post('/login', data=json.dumps(login_data), content_type='application/json')
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['error'] == 'Invalid credentials'
 """
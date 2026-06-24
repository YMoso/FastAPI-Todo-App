from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == 'dziabtest'
    assert response.json()['email'] == 'dziabdziak@gmail.com'
    assert response.json()['first_name'] == 'dziabdziak'
    assert response.json()['last_name'] == 'dziabdziak'
    assert response.json()['phone_number'] == '12345678'
    assert response.json()['role'] == 'admin'


def test_change_password_success(test_user):
    response = client.put("/user/change-password", json={'password': 'testpassword', 'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put("/user/change-password", json={'password': 'wrongpassword', 'new_password': 'newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Invalid password'}

def test_change_phone_number_success(test_user):
    response = client.put("/user/phone-number/2222222222", json={'phone_number': '987654321'})
    assert response.status_code == status.HTTP_204_NO_CONTENT
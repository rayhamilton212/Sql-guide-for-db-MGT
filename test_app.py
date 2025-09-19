import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


def test_index_get(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"What time is it?" in response.data

def test_index_post(client):
    """Test that submitting the time brings the user to the confirmation page."""
    response = client.post('/', data={'time': '4 pm'})
    assert response.status_code == 200
    assert b"You said the time is 4 pm" in response.data
    assert b"Is this correct?" in response.data

def test_confirm_yes(client):
    """Test the confirmation logic for a 'yes' answer."""
    response = client.post('/confirm', data={'confirmation': 'yes'})
    assert response.status_code == 200
    assert b"The time has been confirmed." in response.data

def test_confirm_no(client):
    """Test the confirmation logic for a 'no' answer."""
    response = client.post('/confirm', data={'confirmation': 'no'})
    assert response.status_code == 200
    assert b"The time was not confirmed." in response.data

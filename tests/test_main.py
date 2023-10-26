from bike_rent.main import app
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World :)" in response.data

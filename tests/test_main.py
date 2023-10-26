import sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from main import hello_world
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello World :)" in response.data

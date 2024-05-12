import pytest

from loadbalancer import loadbalancer

@pytest.fixture
def client():
    with loadbalancer.test_client() as client:
        yield client

def test_host_routing_server(client):
    result = client.get('/', headers={'Host': 'www.myservers.com'})
    assert b'This is the server application' in result.data

def test_host_routing_notfound(client):
    result = client.get('/', headers={'Host': 'www.notfound.com'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code

def test_path_routing_server(client):
    result = client.get('/apple')
    assert b'This is the server application.' in result.data


def test_path_routing_notfound(client):
    result = client.get('/notmango')
    assert b'Not Found' in result.data
    assert 404 == result.status_code
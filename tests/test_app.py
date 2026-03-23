import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_valid_input(client):
    response = client.post("/group-anagrams",json={"words": ["eat", "tea"]})
    assert response.status_code == 200

def test_empty_list(client):
    response = client.post("/group-anagrams",json={"words": []})
    assert response.status_code == 200

def test_invalid_not_a_list(client):
    response = client.post("/group-anagrams",json={"words": 543})
    assert response.status_code == 400

def test_invalid_contains_non_strings(client):
    response = client.post("/group-anagrams",json={"words": ["eat", 123]})
    assert response.status_code == 400

def test_missing_words_key(client):
    response = client.post("/group-anagrams",json={"body":["eat", "tea"]})
    assert response.status_code == 400
    
def test_limiting(client):
    response = client.post("/group-anagrams",json={"body":"a"*1_500_000})
    assert response.status_code == 413

def test_unknown_route(client):
    response = client.get("/unknown-route")
    assert response.status_code == 302
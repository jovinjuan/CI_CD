import pytest
from app import app as flask_app, inventory

@pytest.fixture
def test_client():
    flask_app.config['TESTING'] = True
    
    with flask_app.test_client() as client:
        inventory.clear()
        inventory.extend([
            {"id": 1, "nama": "MacBook Pro M2", "stok": 5, "kategori": "Elektronik"},
            {"id": 2, "nama": "Mouse Wireless", "stok": 15, "kategori": "Elektronik"}
        ])
        yield client 

def test_index(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"MacBook Pro M2" in response.data
    assert b"Mouse Wireless" in response.data

def test_additem(test_client):
    new_data = {"nama": "Monitor 4K", "stok": "3", "kategori": "Elektronik"}
    
    response = test_client.post('/add', data=new_data, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Monitor 4K" in response.data 
    assert len(inventory) == 3

def test_delete_item_success(test_client):
    response = test_client.get('/delete/1', follow_redirects=True)
    
    assert response.status_code == 200
    assert b"MacBook Pro M2" not in response.data
    assert len(inventory) == 1

def test_add_item_invalid_data(test_client):
    invalid_data = {"nama": "Keyboard", "stok": "abc", "kategori": "Aksesoris"}
    
    with pytest.raises(ValueError):
        test_client.post('/add', data=invalid_data)
    

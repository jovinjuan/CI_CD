import unittest
from app import app as flask_app, inventory

class InventoryTestCase(unittest.TestCase):

    def setUp(self):
        flask_app.config['TESTING'] = True
        self.client = flask_app.test_client()
        
        inventory.clear()
        inventory.extend([
            {"id": 1, "nama": "MacBook Pro M2", "stok": 5, "kategori": "Elektronik"},
            {"id": 2, "nama": "Mouse Wireless", "stok": 15, "kategori": "Elektronik"}
        ])

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"MacBook Pro M2", response.data)
        self.assertIn(b"Mouse Wireless", response.data)

    def test_add_item(self):
        new_data = {"nama": "Monitor 4K", "stok": "3", "kategori": "Elektronik"}
        response = self.client.post('/add', data=new_data, follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Monitor 4K", response.data)
        self.assertEqual(len(inventory), 3)

    def test_delete_item_success(self):
        response = self.client.get('/delete/1', follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b"MacBook Pro M2", response.data)
        self.assertEqual(len(inventory), 1)

    def test_add_item_invalid_data(self):
        invalid_data = {"nama": "Keyboard", "stok": "abc", "kategori": "Aksesoris"}
        
        with self.assertRaises(ValueError):
            self.client.post('/add', data=invalid_data)

if __name__ == '__main__':
    unittest.main()
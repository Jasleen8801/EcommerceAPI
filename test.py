import unittest
import requests

BASE_URL = 'http://localhost:8000'  

class APITestCase(unittest.TestCase):
    def test_get_products(self):
        response = requests.get(f"{BASE_URL}/api/products")
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        data = {
            "items": [
                {"productId": 1, "boughtQuantity": 2},
                {"productId": 2, "boughtQuantity": 1}
            ],
            "user_address": {
                "City": "New York",
                "Country": "USA",
                "Zip Code": "10001"
            }
        }
        response = requests.post(f"{BASE_URL}/api/orders", json=data)
        self.assertEqual(response.status_code, 200)

    def test_get_orders(self):
        response = requests.get(f"{BASE_URL}/api/orders")
        self.assertEqual(response.status_code, 200)

    def test_get_order(self):
        order_id = "64a93dbbd4967afe9c4005d6"  
        response = requests.get(f"{BASE_URL}/api/orders/{order_id}")
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product_id = "1"  
        data = {"quantity": 40}
        response = requests.put(f"{BASE_URL}/api/products/{product_id}", json=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

import unittest
from app import app


class TestFibonacciAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_fibonacci_zero(self):
        response = self.client.get('/0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 0)

    def test_fibonacci_1(self):
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), 1)
        
if __name__ == '__main__':
    unittest.main()

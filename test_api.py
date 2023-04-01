import unittest
import requests


class TestAPI(unittest.TestCase):
    def test_similar_images(self):
        url = 'http://localhost:5000/similar-images'
        files = {'image': open('assets/shoe0.png', 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.status_code, 200)

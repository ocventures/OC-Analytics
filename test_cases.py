import unittest
import requests

class MicroAnalyticsTests(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:5000"

    def test_home_page(self):
        response = requests.get(f"{self.url}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Micro Analytics Platform", response.text)

    def test_track_pageview(self):
        response = requests.post(f"{self.url}/track", json={"event_type": "pageview", "url": "https://example.com/home"})
        self.assertEqual(response.status_code, 201)

    def test_track_click(self):
        response = requests.post(f"{self.url}/track", json={"event_type": "click", "button": "About Us"})
        self.assertEqual(response.status_code, 201)

    def test_invalid_event_type(self):
        response = requests.post(f"{self.url}/track", json={"event_type": "invalid", "data": "Some data"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid event type", response.text)

if __name__ == '__main__':
    unittest.main()

from django.test import TestCase
from rest_framework.test import APIClient
from shortner.models import Url


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.primary_url = Url.objects.create(url_full="http://www.google.com", url_hash="vrau")

    def test_url_exists(self):
        result = self.client.get("/vrau")
        self.assertEquals(302, result.status_code)

    def test_url_not_found(self):
        result = self.client.get("/vrau2")
        self.assertEquals(404, result.status_code)

    def test_create_url(self):
        url = {
            "url_full": "http://fb.com"
        }
        result = self.client.post("/api/", data=url)
        self.assertEquals(200, result.status_code)
        self.assertIsNotNone(result.json().get("url"))

    def test_create_url_with_hash(self):
        url = {
            "url_full": "http://facebook.com",
            "url_hash": "fb"
        }
        result = self.client.post("/api/", data=url)
        self.assertEquals(200, result.status_code)
        self.assertIsNotNone(result.json().get("url"))

    def test_create_url_with_duplicate_hash(self):
        url = {
            "url_full": "http://fb.com",
            "url_hash": "fb"
        }
        result = self.client.post("/api/", data=url)
        self.assertEquals(200, result.status_code)
            
        result = self.client.post("/api/", data=url)
        self.assertEquals(400, result.status_code)

    def test_create_url_with_hash_and_date(self):
        url = {
            "url_full": "http://facebook.com",
            "url_hash": "fb",
            "expired_at": "2021-08-01 00:00"
        }
        result = self.client.post("/api/", data=url)
        self.assertEquals(200, result.status_code)
        self.assertIsNotNone(result.json().get("url"))
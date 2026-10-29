"""End-to-end ASGI smoke checks for the Kindred Labs FastAPI site."""

import unittest

from fastapi.testclient import TestClient

from app.main import app


class ApiSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app, raise_server_exceptions=True)

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

    def test_home_page_returns_html(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertIn("text/html", response.headers["content-type"])
        self.assertIn("<html", response.text.lower())

    def test_openapi_includes_public_routes(self):
        response = self.client.get("/openapi.json")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertIn("/api/v1/items/", data["paths"])
        self.assertIn("/api/v1/items/{item_id}", data["paths"])

    def test_items_list_contract(self):
        response = self.client.get("/api/v1/items/")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["total"], 3)
        self.assertEqual(len(data["data"]), 3)
        self.assertTrue(data["timestamp"])

    def test_item_detail_contract(self):
        response = self.client.get("/api/v1/items/7")
        self.assertEqual(response.status_code, 200, response.text)
        data = response.json()
        self.assertEqual(data["item"], {"id": 7, "name": "Sample Item 7", "value": 700})
        self.assertTrue(data["timestamp"])

    def test_invalid_item_id_is_rejected(self):
        response = self.client.get("/api/v1/items/not-an-int")
        self.assertEqual(response.status_code, 422, response.text)


if __name__ == "__main__":
    unittest.main(verbosity=2)

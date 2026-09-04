from django.test import TestCase
from django.urls import reverse

from .services import lookup_word


class LookupServiceTests(TestCase):
    def test_lookup_word_returns_lemma(self):
        result = lookup_word("gingen")

        self.assertEqual(result["word"], "gingen")
        self.assertEqual(result["lemma"], "gehen")
        self.assertEqual(result["pos"], "VERB")

    def test_lookup_word_returns_morphology(self):
        result = lookup_word("gingen")

        self.assertIn("morphology", result)
        self.assertEqual(result["morphology"]["Tense"], "Past")
        self.assertEqual(result["morphology"]["Number"], "Plur")
        self.assertEqual(result["morphology"]["Person"], "3")


class LookupAPITests(TestCase):
    def test_lookup_endpoint_returns_json(self):
        response = self.client.get(
            reverse("lookup"),
            {"word": "gingen"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")

        data = response.json()

        self.assertEqual(data["word"], "gingen")
        self.assertEqual(data["lemma"], "gehen")
        self.assertEqual(data["pos"], "VERB")

    def test_lookup_endpoint_rejects_missing_word(self):
        response = self.client.get(reverse("lookup"))

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_lookup_endpoint_rejects_empty_word(self):
        response = self.client.get(
            reverse("lookup"),
            {"word": "   "},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_lookup_endpoint_rejects_long_word(self):
        word = "a" * 101

        response = self.client.get(
            reverse("lookup"),
            {"word": word},
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_lookup_endpoint_requires_get(self):
        response = self.client.post(
            reverse("lookup"),
            {"word": "gingen"},
        )

        self.assertEqual(response.status_code, 405)


class HealthAPITests(TestCase):
    def test_health_endpoint(self):
        response = self.client.get(reverse("health"))

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "ok")
        self.assertTrue(data["spacy"])
        self.assertEqual(data["model"], "de_core_news_sm")



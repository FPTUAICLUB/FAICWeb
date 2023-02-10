from django.test import SimpleTestCase
from django.urls import reverse


class ContactpageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("contact:index")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "contact/index.html")

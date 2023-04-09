from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def setUp(self):
        home_url = reverse("home:index")
        login_url = reverse("home:login")
        self.home_response = self.client.get(home_url)
        self.login_response = self.client.get(login_url)

    def test_homepage_status_code(self):
        self.assertEqual(self.home_response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.home_response, "home/index.html")

    def test_loginpage_status_code(self):
        self.assertEqual(self.login_response.status_code, 200)

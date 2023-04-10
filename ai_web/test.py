from django.test import TestCase
from django.urls import reverse, resolve

class UrlPatternsTest(TestCase):
    def test_admin_url_pattern(self):
        url = reverse("admin:index")
        self.assertEqual(resolve(url).view_name, "admin:index")

    def test_blog_url_pattern(self):
        url = reverse("blog:index")
        self.assertEqual(resolve(url).url_name, "index")

    def test_about_url_pattern(self):
        url = reverse("about:index")
        self.assertEqual(resolve(url).url_name, "index")

    def test_contact_url_pattern(self):
        url = reverse("contact:index")
        self.assertEqual(resolve(url).url_name, "index")

    def test_home_url_pattern(self):
        url = reverse("home:index")
        self.assertEqual(resolve(url).url_name, "index")

class ErrorsTest(TestCase):
    def setUp(self):
        self.expected_text = 'Page Not Found'
        #  non_exist_url = reverse("home:falsdj")
        self.non_exist_reponse = self.client.get('/hiae/')

    def test_non_exist_status_code(self):
        self.assertEqual(self.non_exist_reponse.status_code, 200)

    def test_non_exist_expected_text(self):
        self.assertContains(self.non_exist_reponse, self.expected_text, status_code=200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.non_exist_reponse, "errors/404.html")


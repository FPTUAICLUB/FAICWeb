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

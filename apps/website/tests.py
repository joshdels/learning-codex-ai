from django.contrib.staticfiles import finders
from django.test import SimpleTestCase
from django.urls import reverse


class WebsiteTests(SimpleTestCase):
    def test_pages_render_with_shared_layout(self):
        for name, path, template in [
            ("home", "/", "website/home.html"),
            ("about", "/about/", "website/about.html"),
        ]:
            with self.subTest(page=name):
                self.assertEqual(reverse(f"website:{name}"), path)
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
                self.assertTemplateUsed(response, "base.html")
                self.assertContains(response, "TopMap Solutions")
                self.assertContains(response, 'href="/about/"')
                self.assertContains(response, 'href="/"')

    def test_stylesheet_is_discoverable(self):
        self.assertIsNotNone(finders.find("website/css/style.css"))

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class PageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
        self.assertContains(self.response, 'Pagina Inicial')

    def test_home_page_view(self):
        view = resolve('/')
        self.assertEqual(view.func.view_class, HomePageView)
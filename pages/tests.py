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


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
        self.assertContains(self.response, 'About Us')

    def test_page_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_view(self):
        view = resolve('about')
        self.assertEqual(view.func.view_class, AboutPageView)


class TrainersPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('trainers')
        self.response = self.client.get(url)

    def test_treiners_pages_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_treiners_page_template(self):
        self.assertTemplateUsed(self.response, 'trainers.html')
        self.assertContains(self.response, 'Trainers')

    def test_profile_name(self):
        self.assertEqual(self.response_code, 200)

    def test_treiners_page_view(self):
        view = resolve('trainers')
        self.assertEqual(view.func.view_class, TrainersPageView)

        


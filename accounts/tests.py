from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from accounts.views import SignUpView
from accounts.forms import CustomUserCreationForm

CustomUser = get_user_model()

class CustomUserTest(TestCase):
    def setUp(self): 
        self.user = CustomUser.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='test123'
        )

        self.super_user = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='admin123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.email, 'test@gmail.com')
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_active)

    def test_super_user_creation(self):
        self.assertEqual(self.super_user.username, 'admin')
        self.assertEqual(self.super_user.email, 'admin@gmail.com')
        self.assertTrue(self.super_user.is_superuser)
        self.assertTrue(self.super_user.is_active)


class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_signup_template(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Cadastrar')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(view.func.__name__, SignUpView.as_view().__name__)
        

class ProfilePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('profile')
        self.response = self.client.get(url)

    def test_profile_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_profile_page_template(self):
        self.assertTemplateUsed(self.response, 'registration/profile.html')
        self.assertContains(self.response, 'Profile')

    def test_profile_name(self):
        self.assertEqual(self.response_code, 200)

    def test_profile_page_view(self):
        view = reverse('profile')
        self.assertEqual(view.func.__name__, ProfileView.as_view().__name__)
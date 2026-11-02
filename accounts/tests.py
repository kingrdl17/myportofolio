from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountViewTests(TestCase):
    def test_register_page_is_accessible(self):
        response = self.client.get(reverse("accounts:register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/accounts/register.html")
        self.assertContains(response, "focus:outline-2")

    def test_registration_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "new-portfolio-user",
                "password1": "L0ng-test-password-481",
                "password2": "L0ng-test-password-481",
            },
        )

        self.assertRedirects(response, reverse("accounts:login"))
        self.assertTrue(User.objects.filter(username="new-portfolio-user").exists())

    def test_login_and_logout(self):
        user = User.objects.create_user(username="portfolio-user", password="safe-test-password")

        response = self.client.post(
            reverse("accounts:login"),
            {"username": user.username, "password": "safe-test-password"},
        )

        self.assertRedirects(response, reverse("profiles:show_main"))
        self.assertIn("last_login", response.cookies)

        response = self.client.get(reverse("accounts:logout"))

        self.assertRedirects(response, reverse("profiles:show_main"))
        self.assertEqual(response.cookies["last_login"].value, "")

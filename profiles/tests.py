from django.test import TestCase
from django.urls import reverse


class ProfilePageTests(TestCase):
    def test_profile_page_is_accessible(self):
        response = self.client.get(reverse("profiles:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/profile/index.html")
        self.assertTemplateUsed(response, "components/navbar.html")
        self.assertTemplateUsed(response, "components/footer.html")
        self.assertContains(response, "Marclay Ardell")
        self.assertContains(response, "css/dist/styles.css")
        self.assertContains(
            response,
            '<div class="mx-auto max-w-[960px] rounded-3xl border border-white/[0.12]',
        )

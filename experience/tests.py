from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Experience


class ExperienceFeatureTests(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_experience_page_and_json(self):
        page = self.client.get(reverse("experience:show_experience"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "pages/experience/index.html")
        self.assertTemplateUsed(page, "components/experience_delete_modal.html")
        self.assertContains(page, 'id="delete-confirmation-template"')
        self.assertContains(page, "open:block")
        self.assertContains(page, 'src="/static/js/delete-modal.js"')
        self.assertNotContains(page, "onclick=\"return confirm(")

        response = self.client.get(reverse("experience:get_experience_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["title"], self.experience.title)
        self.assertIsNone(response.json()[0]["fields"]["ended_at"])

    def test_completed_experience_is_serialized(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(reverse("experience:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertIsNotNone(response.json()[0]["fields"]["ended_at"])

    def test_experience_model_and_filter(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertTrue(self.experience.is_ongoing)

        response = self.client.get(reverse("experience:get_experience_json"), {"title": "missing"})
        self.assertEqual(response.json(), [])

    def test_authenticated_user_can_toggle_star(self):
        user = User.objects.create_user(username="star-user", password="safe-test-password")
        self.client.force_login(user)
        url = reverse("experience:toggle_star", kwargs={"experience_id": self.experience.id})

        self.client.post(url)
        self.assertTrue(self.experience.starred_by.filter(pk=user.pk).exists())
        self.client.post(url)
        self.assertFalse(self.experience.starred_by.filter(pk=user.pk).exists())

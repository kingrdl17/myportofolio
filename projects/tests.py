from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Project


class ProjectFeatureTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            project_name="Portfolio",
            project_description="A Django portfolio",
            category="web development",
            technologies_used="Django, Tailwind",
            project_link="https://example.com",
        )

    def test_projects_page_and_json(self):
        page = self.client.get(reverse("projects:show_project"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "pages/project/index.html")
        self.assertTemplateUsed(page, "components/project_delete_modal.html")
        self.assertContains(page, 'id="delete-confirmation-template"')
        self.assertContains(page, "open:block")
        self.assertContains(page, 'src="/static/js/delete-modal.js?v=2"')
        self.assertNotContains(page, "onclick=\"return confirm(")
        self.assertNotContains(page, "window.confirm(")
        self.assertContains(page, "window.confirmDelete()")

        response = self.client.get(reverse("projects:get_project_json"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["project_name"], self.project.project_name)

    def test_completed_projects_is_serialized(self):
        response = self.client.get(reverse("projects:get_project_json"))
        self.assertEqual(response.status_code, 200)

    def test_projects_model_and_filter(self):
        self.assertEqual(str(self.project), "Portfolio")

        response = self.client.get(reverse("projects:get_project_json"), {"title": "missing"})
        self.assertEqual(response.json(), [])

    def test_authenticated_user_can_toggle_star(self):
        user = User.objects.create_user(username="star-user", password="safe-test-password")
        self.client.force_login(user)
        url = reverse("projects:toggle_project_star", kwargs={"project_id": self.project.id})

        self.client.post(url)
        self.assertTrue(self.project.starred_by.filter(pk=user.pk).exists())
        self.client.post(url)
        self.assertFalse(self.project.starred_by.filter(pk=user.pk).exists())

from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Education


class EducationFeatureTests(TestCase):
    def setUp(self):
        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="S1",
            field_of_study="Sistem Informasi",
            started_at=date(2022, 8, 1),
        )

    def test_education_page_and_json(self):
        page = self.client.get(reverse("education:show_education"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "pages/education/index.html")
        self.assertTemplateUsed(page, "components/education_delete_modal.html")
        self.assertContains(page, 'id="delete-confirmation-template"')
        self.assertContains(page, "open:block")
        self.assertContains(page, 'src="/static/js/delete-modal.js?v=2"')
        self.assertNotContains(page, "onclick=\"return confirm(")
        self.assertNotContains(page, "window.confirm(")
        self.assertContains(page, "window.confirmDelete()")
        self.assertContains(page, f'href="{reverse("profiles:show_main")}"')

        response = self.client.get(reverse("education:get_education_json"), {"title": "Indonesia"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["institution"], "Universitas Indonesia")

    def test_education_model(self):
        self.assertEqual(str(self.education), "S1 at Universitas Indonesia")
        self.assertTrue(self.education.is_ongoing)

    def test_search_filters_education_json(self):
        response = self.client.get(reverse("education:get_education_json"), {"title": "missing"})
        self.assertEqual(response.json(), [])

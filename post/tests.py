from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostFeatureTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Portfolio update",
            image_url="https://example.com/post.jpg",
            content="A new post",
            category="technology",
        )

    def test_post_page_and_json(self):
        page = self.client.get(reverse("post:show_post"))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "pages/post/index.html")
        self.assertTemplateUsed(page, "components/post_delete_modal.html")
        self.assertContains(page, 'id="delete-confirmation-template"')
        self.assertContains(page, "open:block")
        self.assertContains(page, 'src="/static/js/delete-modal.js?v=2"')
        self.assertNotContains(page, "onclick=\"return confirm(")
        self.assertNotContains(page, "window.confirm(")
        self.assertContains(page, "window.confirmDelete()")
        self.assertContains(page, f'href="{reverse("profiles:show_main")}"')

        response = self.client.get(reverse("post:get_post_json"), {"title": "Portfolio"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]["fields"]["title"], "Portfolio update")

    def test_post_model(self):
        self.assertEqual(str(self.post), "Portfolio update")

    def test_search_filters_post_json(self):
        response = self.client.get(reverse("post:get_post_json"), {"title": "missing"})
        self.assertEqual(response.json(), [])

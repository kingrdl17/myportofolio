from django.test import SimpleTestCase
from django.urls import reverse


class LegacyMainRouteTests(SimpleTestCase):
    def test_legacy_route_names_preserve_existing_paths(self):
        route_pairs = (
            ("show_main", "profiles:show_main"),
            ("show_post", "post:show_post"),
            ("show_projects", "projects:show_projects"),
            ("create_post", "post:create_post"),
            ("create_projects", "projects:create_projects"),
            ("get_post_json", "post:get_post_json"),
            ("get_projects_json", "projects:get_projects_json"),
            ("create_post_ajax", "post:create_post_ajax"),
            ("create_projects_ajax", "projects:create_projects_ajax"),
            ("register", "accounts:register"),
            ("login", "accounts:login"),
            ("logout", "accounts:logout"),
        )

        for legacy_name, feature_name in route_pairs:
            with self.subTest(route=legacy_name):
                self.assertEqual(reverse(f"main:{legacy_name}"), reverse(feature_name))

    def test_legacy_object_routes_preserve_existing_paths(self):
        route_pairs = (
            ("edit_post", "post:edit_post", {"post_id": "00000000-0000-0000-0000-000000000001"}),
            ("delete_post", "post:delete_post", {"post_id": "00000000-0000-0000-0000-000000000001"}),
            ("edit_projects", "projects:edit_projects", {"projects_id": "00000000-0000-0000-0000-000000000002"}),
            ("delete_projects", "projects:delete_projects", {"projects_id": "00000000-0000-0000-0000-000000000002"}),
            ("toggle_star", "projects:toggle_star", {"projects_id": "00000000-0000-0000-0000-000000000002"}),
        )

        for legacy_name, feature_name, kwargs in route_pairs:
            with self.subTest(route=legacy_name):
                self.assertEqual(
                    reverse(f"main:{legacy_name}", kwargs=kwargs),
                    reverse(feature_name, kwargs=kwargs),
                )

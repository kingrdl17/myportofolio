from django.test import SimpleTestCase
from django.urls import reverse


class LegacyMainRouteTests(SimpleTestCase):
    def test_legacy_route_names_preserve_existing_paths(self):
        route_pairs = (
            ("show_main", "profiles:show_main"),
            ("show_education", "education:show_education"),
            ("show_experience", "experience:show_experience"),
            ("create_education", "education:create_education"),
            ("create_experience", "experience:create_experience"),
            ("get_education_json", "education:get_education_json"),
            ("get_experience_json", "experience:get_experience_json"),
            ("create_education_ajax", "education:create_education_ajax"),
            ("create_experience_ajax", "experience:create_experience_ajax"),
            ("register", "accounts:register"),
            ("login", "accounts:login"),
            ("logout", "accounts:logout"),
        )

        for legacy_name, feature_name in route_pairs:
            with self.subTest(route=legacy_name):
                self.assertEqual(reverse(f"main:{legacy_name}"), reverse(feature_name))

    def test_legacy_object_routes_preserve_existing_paths(self):
        route_pairs = (
            ("edit_education", "education:edit_education", {"education_id": "00000000-0000-0000-0000-000000000001"}),
            ("delete_education", "education:delete_education", {"education_id": "00000000-0000-0000-0000-000000000001"}),
            ("edit_experience", "experience:edit_experience", {"experience_id": "00000000-0000-0000-0000-000000000002"}),
            ("delete_experience", "experience:delete_experience", {"experience_id": "00000000-0000-0000-0000-000000000002"}),
            ("toggle_star", "experience:toggle_star", {"experience_id": "00000000-0000-0000-0000-000000000002"}),
        )

        for legacy_name, feature_name, kwargs in route_pairs:
            with self.subTest(route=legacy_name):
                self.assertEqual(
                    reverse(f"main:{legacy_name}", kwargs=kwargs),
                    reverse(feature_name, kwargs=kwargs),
                )

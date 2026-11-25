from django.urls import path

from . import views

app_name = "education"

urlpatterns = [
    path("post/", views.show_post, name="show_post"),
    path("post/add/", views.create_post, name="create_post"),
    path("post/edit/<uuid:post_id>/", views.edit_post, name="edit_post"),
    path("post/delete/<uuid:post_id>/", views.delete_post, name="delete_post"),
    path("api/posts/", views.get_post_json, name="get_post_json"),
    path("post/add-ajax/", views.create_post_ajax, name="create_post_ajax"),
    path("education/", views.show_education, name="show_education"),
    path("education/add/", views.create_education, name="create_education"),
    path("education/edit/<uuid:education_id>/", views.edit_education, name="edit_education"),
    path("education/delete/<uuid:education_id>/", views.delete_education, name="delete_education"),
    path("api/educations/", views.get_education_json, name="get_education_json"),
    path("education/add-ajax/", views.create_education_ajax, name="create_education_ajax"),
]

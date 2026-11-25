from django.urls import path

from . import views

app_name = "post"

urlpatterns = [
    path("post/", views.show_post, name="show_post"),
    path("post/add/", views.create_post, name="create_post"),
    path("post/edit/<uuid:post_id>/", views.edit_post, name="edit_post"),
    path("post/delete/<uuid:post_id>/", views.delete_post, name="delete_post"),
    path("api/posts/", views.get_post_json, name="get_post_json"),
    path("post/add-ajax/", views.create_post_ajax, name="create_post_ajax"),
]

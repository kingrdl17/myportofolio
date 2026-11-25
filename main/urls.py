from django.urls import path

from main.views import (
    create_post,
    create_post_ajax,
    create_project,
    create_project_ajax,
    delete_post,
    delete_project,
    edit_post,
    edit_project,
    get_post_json,
    get_project_json,
    login_user,
    logout_user,
    register,
    show_main,
    show_post,
    show_project,
    toggle_project_star,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("post/", show_post, name="show_post"),
    path("project/", show_project, name="show_project"),
    path("post/add/", create_post, name="create_post"),
    path("project/add/", create_project, name="create_project"),
    path("post/edit/<uuid:post_id>/", edit_post, name="edit_post"),
    path("project/edit/<uuid:project_id>/", edit_project, name="edit_project"),
    path("post/delete/<uuid:post_id>/", delete_post, name="delete_post"),
    path("project/delete/<uuid:project_id>/", delete_project, name="delete_project"),
    path("api/posts/", get_post_json, name="get_post_json"),
    path("api/projects/", get_project_json, name="get_project_json"),
    path("project/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("post/add-ajax/", create_post_ajax, name="create_post_ajax"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_project_star, name="toggle_project_star"),
]

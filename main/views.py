from accounts.views import login_user, logout_user, register
from post.views import (
    create_post,
    create_post_ajax,
    delete_post,
    edit_post,
    get_post_json,
    show_post,
)
from projects.views import (
    create_project,
    create_project_ajax,
    delete_project,
    edit_project,
    get_project_json,
    show_project,
    toggle_project_star,
)
from profiles.views import show_main

__all__ = [
    "create_post",
    "create_post_ajax",
    "create_project",
    "create_project_ajax",
    "delete_post",
    "delete_project",
    "edit_post",
    "edit_project",
    "get_post_json",
    "get_project_json",
    "login_user",
    "logout_user",
    "register",
    "show_post",
    "show_project",
    "show_main",
    "toggle_project_star",
]

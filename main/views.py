from accounts.views import login_user, logout_user, register
from education.views import (
    create_education,
    create_education_ajax,
    delete_education,
    edit_education,
    get_education_json,
    show_education,
)
from experience.views import (
    create_experience,
    create_experience_ajax,
    delete_experience,
    edit_experience,
    get_experience_json,
    show_experience,
    toggle_star,
)
from profiles.views import show_main

__all__ = [
    "create_education",
    "create_education_ajax",
    "create_experience",
    "create_experience_ajax",
    "delete_education",
    "delete_experience",
    "edit_education",
    "edit_experience",
    "get_education_json",
    "get_experience_json",
    "login_user",
    "logout_user",
    "register",
    "show_education",
    "show_experience",
    "show_main",
    "toggle_star",
]

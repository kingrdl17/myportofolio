from django.urls import path

from main.views import (
    show_main, 
    show_experience, 
    show_education,
    create_education, 
    get_education_json, 
    delete_education,
    create_experience, 
    delete_experience, 
    get_experience_json,
    edit_education, 
    edit_experience,
    register,
    login_user,
    logout_user,
    toggle_star
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),

    path("education/add/", create_education, name="create_education"),
    path("experience/add/", create_experience, name="create_experience"),
    path("education/edit/<uuid:education_id>/", edit_education, name="edit_education"),
    path("experience/edit/<uuid:experience_id>/", edit_experience, name="edit_experience"),

    path("education/delete/<uuid:education_id>/", delete_education, name="delete_education"),
    path("experience/delete/<uuid:experience_id>/", delete_experience, name="delete_experience"),

    path("api/educations/", get_education_json, name="get_education_json"),
    path("api/experiences/", get_experience_json, name="get_experience_json"),

    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path(
    "experiences/<uuid:experience_id>/star/",
    toggle_star,
    name="toggle_star",
    ),
]
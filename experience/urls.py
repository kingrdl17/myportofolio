from django.urls import path

from . import views

app_name = "experience"

urlpatterns = [
    path("experience/", views.show_experience, name="show_experience"),
    path("experience/add/", views.create_experience, name="create_experience"),
    path("experience/edit/<uuid:experience_id>/", views.edit_experience, name="edit_experience"),
    path("experience/delete/<uuid:experience_id>/", views.delete_experience, name="delete_experience"),
    path("api/experiences/", views.get_experience_json, name="get_experience_json"),
    path("experience/add-ajax/", views.create_experience_ajax, name="create_experience_ajax"),
    path("experiences/<uuid:experience_id>/star/", views.toggle_star, name="toggle_star"),
]

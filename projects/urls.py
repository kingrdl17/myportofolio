from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("project/", views.show_project, name="show_project"),
    path("project/add/", views.create_project, name="create_project"),
    path("project/edit/<uuid:project_id>/", views.edit_project, name="edit_project"),
    path("project/delete/<uuid:project_id>/", views.delete_project, name="delete_project"),
    path("api/projects/", views.get_project_json, name="get_project_json"),
    path("project/add-ajax/", views.create_project_ajax, name="create_project_ajax"),
    path("projects/<uuid:project_id>/star/", views.toggle_project_star, name="toggle_project_star"),
]

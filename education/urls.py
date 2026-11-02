from django.urls import path

from . import views

app_name = "education"

urlpatterns = [
    path("education/", views.show_education, name="show_education"),
    path("education/add/", views.create_education, name="create_education"),
    path("education/edit/<uuid:education_id>/", views.edit_education, name="edit_education"),
    path("education/delete/<uuid:education_id>/", views.delete_education, name="delete_education"),
    path("api/educations/", views.get_education_json, name="get_education_json"),
    path("education/add-ajax/", views.create_education_ajax, name="create_education_ajax"),
]

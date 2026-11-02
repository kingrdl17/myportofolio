from django.urls import path

from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.show_main, name="show_main"),
]

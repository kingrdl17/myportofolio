from django.urls import path
from main import api_views
from rest_framework.authtoken import views as authtoken_views

app_name = "api"

urlpatterns = [
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    path("posts/", api_views.post_list, name="post-list"),
    path("posts/<uuid:post_id>/", api_views.post_detail, name="post-detail"),
    path("posts/<uuid:post_id>/star/", api_views.post_star, name="post-star"),

    # Auth endpoints
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_token_logout"),
]

from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "category", "project_link")
    list_filter = ("category",)
    search_fields = ("project_name", "project_description", "technologies_used")

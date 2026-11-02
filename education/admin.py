from django.contrib import admin

from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("institution", "degree", "field_of_study", "started_at", "ended_at", "is_ongoing")
    list_filter = ("degree",)
    search_fields = ("institution", "degree", "field_of_study", "description")

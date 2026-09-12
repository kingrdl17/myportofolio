from django.contrib import admin
from .models import Experience, Education

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'started_at', 'ended_at', 'is_ongoing')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    readonly_fields = ('started_at',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'field_of_study', 'started_at', 'ended_at', 'is_ongoing')
    list_filter = ('degree',)
    search_fields = ('institution', 'degree', 'field_of_study', 'description')

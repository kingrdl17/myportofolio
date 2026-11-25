from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from .models import Project

FORM_CONTROL_CLASSES = (
    "w-full rounded-xl border border-[#0a84ff] bg-[rgba(30,30,30,0.75)] p-3 "
    "font-sans text-[#f5f5f7] focus:border-[#0a84ff] focus:outline "
    "focus:outline-2 focus:outline-[#0a84ff]"
)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["project_name", "project_description", "category", "technologies_used", "project_link"]
        labels = {
            "project_name": "Project Name",
            "project_description": "Project Description",
            "category": "Project category",
            "technologies_used": "Technologies used",
            "project_link": "Project Link",
        }
        widgets = {
            "project_name": TextInput(
                attrs={"placeholder": "My project", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "project_description": Textarea(
                attrs={
                    "placeholder": "Describe the project...",
                    "rows": 3,
                    "class": FORM_CONTROL_CLASSES,
                }
            ),
            "technologies_used": Textarea(
                attrs={"placeholder": "Django, JavaScript, PostgreSQL", "rows": 2, "class": FORM_CONTROL_CLASSES}
            ),
            "project_link": URLInput(attrs={"placeholder": "https://example.com", "class": FORM_CONTROL_CLASSES}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs["class"] = FORM_CONTROL_CLASSES

    def clean_project_name(self):
        name = strip_tags(self.cleaned_data["project_name"]).strip()
        if not name:
            raise ValidationError("Project name cannot be empty.")
        return name

    def clean_project_description(self):
        return strip_tags(self.cleaned_data["project_description"]).strip()


ExperienceForm = ProjectForm

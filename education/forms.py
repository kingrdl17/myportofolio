from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from .models import Post

FORM_CONTROL_CLASSES = (
    "w-full rounded-xl border border-[#0a84ff] bg-[rgba(30,30,30,0.75)] p-3 "
    "font-sans text-[#f5f5f7] focus:border-[#0a84ff] focus:outline "
    "focus:outline-2 focus:outline-[#0a84ff]"
)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "image_url",
            "content",
            "category",
        ]
        labels = {
            "title": "Post title",
            "image_url": "Image URL",
            "content": "Post content",
            "category": "Post category",
        }
        widgets = {
            "title": TextInput(
                attrs={"placeholder": "Post title", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "content": Textarea(
                attrs={
                    "placeholder": "Write post content...",
                    "rows": 3,
                    "class": FORM_CONTROL_CLASSES,
                }
            ),
            "image_url": URLInput(attrs={"placeholder": "https://example.com/image.jpg", "class": FORM_CONTROL_CLASSES}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Post title cannot be empty.")
        return title

    def clean_content(self):
        description = self.cleaned_data.get("content")
        return strip_tags(description).strip() if description else description


EducationForm = PostForm

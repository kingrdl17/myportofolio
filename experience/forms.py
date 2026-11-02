from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from .models import Experience

FORM_CONTROL_CLASSES = (
    "w-full rounded-xl border border-[#0a84ff] bg-[rgba(30,30,30,0.75)] p-3 "
    "font-sans text-[#f5f5f7] focus:border-[#0a84ff] focus:outline "
    "focus:outline-2 focus:outline-[#0a84ff]"
)


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "category", "description", "thumbnail", "started_at", "ended_at"]
        labels = {
            "title": "Judul / Posisi",
            "category": "Kategori / Jenis Pengalaman",
            "description": "Deskripsi / Pencapaian",
            "thumbnail": "URL Logo / Gambar",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
        }
        widgets = {
            "title": TextInput(
                attrs={"placeholder": "Software Engineer Intern", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "description": Textarea(
                attrs={
                    "placeholder": (
                        "Ceritakan pengalaman, tanggung jawab, atau pencapaian selama pengalaman ini..."
                    ),
                    "rows": 3,
                    "class": FORM_CONTROL_CLASSES,
                }
            ),
            "thumbnail": URLInput(attrs={"placeholder": "URL Here", "class": FORM_CONTROL_CLASSES}),
            "started_at": DateInput(attrs={"type": "date", "class": FORM_CONTROL_CLASSES}),
            "ended_at": DateInput(attrs={"type": "date", "class": FORM_CONTROL_CLASSES}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["category"].widget.attrs["class"] = FORM_CONTROL_CLASSES

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

from django.core.exceptions import ValidationError
from django.forms import DateInput, ModelForm, TextInput, Textarea, URLInput
from django.utils.html import strip_tags

from .models import Education

FORM_CONTROL_CLASSES = (
    "w-full rounded-xl border border-[#0a84ff] bg-[rgba(30,30,30,0.75)] p-3 "
    "font-sans text-[#f5f5f7] focus:border-[#0a84ff] focus:outline "
    "focus:outline-2 focus:outline-[#0a84ff]"
)


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "institution",
            "degree",
            "field_of_study",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
        ]
        labels = {
            "institution": "Nama Institusi / Universitas",
            "degree": "Gelar / Tingkat",
            "field_of_study": "Jurusan / Bidang Studi",
            "description": "Deskripsi / Pencapaian",
            "thumbnail": "URL Logo / Gambar",
            "started_at": "Tanggal Mulai",
            "ended_at": "Tanggal Selesai",
        }
        widgets = {
            "institution": TextInput(
                attrs={"placeholder": "Universitas Indonesia", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "degree": TextInput(
                attrs={"placeholder": "Sarjana Komputer (S.Kom)", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "field_of_study": TextInput(
                attrs={"placeholder": "Ilmu Komputer", "maxlength": 255, "class": FORM_CONTROL_CLASSES}
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman atau fokus studi selama pendidikan...",
                    "rows": 3,
                    "class": FORM_CONTROL_CLASSES,
                }
            ),
            "thumbnail": URLInput(attrs={"placeholder": "URL Here", "class": FORM_CONTROL_CLASSES}),
            "started_at": DateInput(attrs={"type": "date", "class": FORM_CONTROL_CLASSES}),
            "ended_at": DateInput(attrs={"type": "date", "class": FORM_CONTROL_CLASSES}),
        }

    def clean_institution(self):
        institution = strip_tags(self.cleaned_data["institution"]).strip()
        if not institution:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return institution

    def clean_degree(self):
        degree = self.cleaned_data.get("degree")
        return strip_tags(degree).strip() if degree else degree

    def clean_field_of_study(self):
        field_of_study = self.cleaned_data.get("field_of_study")
        return strip_tags(field_of_study).strip() if field_of_study else field_of_study

    def clean_description(self):
        description = self.cleaned_data.get("description")
        return strip_tags(description).strip() if description else description

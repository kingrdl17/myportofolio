from django.forms import DateInput, ModelForm, TextInput, Textarea, URLInput 

from main.models import Education
from main.models import Experience

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
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "degree": TextInput(
                attrs={
                    "placeholder": "Sarjana Komputer (S.Kom)",
                    "maxlength": 255,
                }
            ),
            "field_of_study": TextInput(
                attrs={
                    "placeholder": "Ilmu Komputer",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pengalaman atau fokus studi selama pendidikan...",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "URL Here",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def clean_institution(self):
        from django.core.exceptions import ValidationError
        from django.utils.html import strip_tags
        institution = strip_tags(self.cleaned_data["institution"]).strip()
        if not institution:
            raise ValidationError("Nama institusi tidak boleh hanya berisi tag HTML.")
        return institution

    def clean_degree(self):
        from django.utils.html import strip_tags
        degree = self.cleaned_data.get("degree")
        return strip_tags(degree).strip() if degree else degree

    def clean_field_of_study(self):
        from django.utils.html import strip_tags
        field_of_study = self.cleaned_data.get("field_of_study")
        return strip_tags(field_of_study).strip() if field_of_study else field_of_study

    def clean_description(self):
        from django.utils.html import strip_tags
        description = self.cleaned_data.get("description")
        return strip_tags(description).strip() if description else description

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "category",
            "description",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

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
                attrs={
                    "placeholder": "Software Engineer Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": (
                        "Ceritakan pengalaman, tanggung jawab, atau pencapaian selama pengalaman ini..."
                    ),
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "URL Here",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
        }

    def clean_title(self):
        from django.core.exceptions import ValidationError
        from django.utils.html import strip_tags
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Judul tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        from django.utils.html import strip_tags
        return strip_tags(self.cleaned_data["description"]).strip()

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
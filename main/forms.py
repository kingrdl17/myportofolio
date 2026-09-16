from django.forms import DateInput, ModelForm, TextInput, Textarea, URLInput 

from main.models import Education

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
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
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
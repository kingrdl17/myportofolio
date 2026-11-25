import uuid
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True
    dependencies = [("main", "0006_experience_starred_by")]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
            name="Project",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("project_name", models.CharField(blank=True, default="", max_length=255)),
                ("project_description", models.TextField(blank=True, default="")),
                ("category", models.CharField(choices=[("web development", "Web Development"), ("mobile development", "Mobile Development"), ("machine learning", "Machine Learning"), ("data science", "Data Science"), ("other", "Other"), ("internship", "Internship"), ("research", "Research"), ("volunteer", "Volunteer"), ("part-time", "Part-Time"), ("full-time", "Full-Time"), ("freelance", "Freelance")], default="other", max_length=30)),
                ("technologies_used", models.TextField(blank=True, default="")),
                ("project_link", models.URLField(blank=True, null=True)),
                ("title", models.CharField(blank=True, default="", max_length=255)),
                ("description", models.TextField(blank=True, default="")),
                ("thumbnail", models.URLField(blank=True, null=True)),
                ("started_at", models.DateTimeField(default=django.utils.timezone.now)),
                ("ended_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={"db_table": "main_experience"},
                ),
            ],
        ),
    ]

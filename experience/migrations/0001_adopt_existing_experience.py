import uuid

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main", "0006_experience_starred_by"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="Experience",
                    fields=[
                        ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                        ("title", models.CharField(max_length=255)),
                        ("description", models.TextField()),
                        (
                            "category",
                            models.CharField(
                                choices=[
                                    ("internship", "Internship"),
                                    ("research", "Research"),
                                    ("volunteer", "Volunteer"),
                                    ("part-time", "Part-Time"),
                                    ("full-time", "Full-Time"),
                                    ("freelance", "Freelance"),
                                ],
                                default="full-time",
                                max_length=20,
                            ),
                        ),
                        ("thumbnail", models.URLField(blank=True, null=True)),
                        ("started_at", models.DateTimeField(default=django.utils.timezone.now)),
                        ("ended_at", models.DateTimeField(blank=True, null=True)),
                        (
                            "starred_by",
                            models.ManyToManyField(
                                blank=True,
                                db_table="main_experience_starred_by",
                                related_name="starred_experiences",
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                    options={"db_table": "main_experience"},
                ),
            ],
        ),
    ]

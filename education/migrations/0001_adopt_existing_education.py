import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("main", "0006_experience_starred_by"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="Education",
                    fields=[
                        ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                        ("institution", models.CharField(max_length=255)),
                        ("degree", models.CharField(blank=True, max_length=255, null=True)),
                        ("field_of_study", models.CharField(blank=True, max_length=255, null=True)),
                        ("description", models.TextField(blank=True, null=True)),
                        ("thumbnail", models.URLField(blank=True, null=True)),
                        ("started_at", models.DateField()),
                        ("ended_at", models.DateField(blank=True, null=True)),
                    ],
                    options={"db_table": "main_education"},
                ),
            ],
        ),
    ]

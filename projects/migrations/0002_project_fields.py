from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("projects", "0001_adopt_existing_experience"), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
        migrations.CreateModel(
            name="ProjectStar",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("project", models.ForeignKey(db_column="experience_id", on_delete=django.db.models.deletion.CASCADE, to="projects.project")),
                ("user", models.ForeignKey(db_column="user_id", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={"db_table": "main_experience_starred_by", "unique_together": {("project", "user")}},
        ),
        migrations.AddField(
            model_name="project",
            name="starred_by",
            field=models.ManyToManyField(blank=True, related_name="starred_projects", through="projects.ProjectStar", through_fields=("project", "user"), to=settings.AUTH_USER_MODEL),
        ),
            ],
        ),
    ]

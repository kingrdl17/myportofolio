import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0001_adopt_existing_experience"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AddField(
                    model_name="experience",
                    name="project_name",
                    field=models.CharField(blank=True, default="", max_length=255),
                ),
                migrations.AddField(
                    model_name="experience",
                    name="project_description",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="experience",
                    name="technologies_used",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="experience",
                    name="project_link",
                    field=models.URLField(blank=True, null=True),
                ),
            ],
            state_operations=[
                migrations.RenameModel(old_name="Experience", new_name="Project"),
                migrations.AlterModelTable(name="Project", table="main_experience"),
                migrations.AddField(
                    model_name="project",
                    name="project_name",
                    field=models.CharField(blank=True, default="", max_length=255),
                ),
                migrations.AddField(
                    model_name="project",
                    name="project_description",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="project",
                    name="technologies_used",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="project",
                    name="project_link",
                    field=models.URLField(blank=True, null=True),
                ),
            ],
        ),
    ]

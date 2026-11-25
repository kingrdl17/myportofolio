from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0002_education_starred_by"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.AddField(
                    model_name="education",
                    name="title",
                    field=models.CharField(blank=True, default="", max_length=255),
                ),
                migrations.AddField(
                    model_name="education",
                    name="image_url",
                    field=models.URLField(blank=True, null=True),
                ),
                migrations.AddField(
                    model_name="education",
                    name="content",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="education",
                    name="category",
                    field=models.CharField(
                        choices=[
                            ("general", "General"),
                            ("information", "Information"),
                            ("fun", "Fun"),
                            ("technology", "Technology"),
                            ("other", "Other"),
                        ],
                        default="general",
                        max_length=20,
                    ),
                ),
            ],
            state_operations=[
                migrations.RenameModel(old_name="Education", new_name="Post"),
                migrations.AlterModelTable(name="Post", table="main_education"),
                migrations.AddField(
                    model_name="post",
                    name="title",
                    field=models.CharField(blank=True, default="", max_length=255),
                ),
                migrations.AddField(
                    model_name="post",
                    name="image_url",
                    field=models.URLField(blank=True, null=True),
                ),
                migrations.AddField(
                    model_name="post",
                    name="content",
                    field=models.TextField(blank=True, default=""),
                ),
                migrations.AddField(
                    model_name="post",
                    name="category",
                    field=models.CharField(
                        choices=[
                            ("general", "General"),
                            ("information", "Information"),
                            ("fun", "Fun"),
                            ("technology", "Technology"),
                            ("other", "Other"),
                        ],
                        default="general",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]

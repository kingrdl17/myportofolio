from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0004_alter_post_institution_alter_post_starred_by_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name="PostStar",
                    fields=[
                        ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                        ("post", models.ForeignKey(db_column="education_id", on_delete=django.db.models.deletion.CASCADE, to="education.post")),
                        ("user", models.ForeignKey(db_column="user_id", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                    ],
                    options={"db_table": "main_education_starred_by", "unique_together": {("post", "user")}},
                ),
                migrations.AlterField(
                    model_name="post",
                    name="starred_by",
                    field=models.ManyToManyField(blank=True, related_name="starred_posts", through="education.PostStar", through_fields=("post", "user"), to=settings.AUTH_USER_MODEL),
                ),
            ],
        ),
    ]

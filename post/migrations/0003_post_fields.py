from django.db import migrations, models


def add_post_columns(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    table = "main_education"
    with schema_editor.connection.cursor() as cursor:
        cursor.execute('PRAGMA table_info("%s")' % table)
        existing = {row[1] for row in cursor.fetchall()}
        columns = [
            ("title", "varchar(255) NOT NULL DEFAULT ''"),
            ("image_url", "varchar(200)"),
            ("content", "text NOT NULL DEFAULT ''"),
            ("category", "varchar(20) NOT NULL DEFAULT 'general'"),
        ]
        for name, definition in columns:
            if name not in existing:
                cursor.execute('ALTER TABLE "%s" ADD COLUMN %s %s' % (table, name, definition))


class Migration(migrations.Migration):
    dependencies = [("post", "0002_education_starred_by")]
    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(add_post_columns, reverse_code=migrations.RunPython.noop),
            ],
            state_operations=[
                migrations.AddField(model_name="post", name="title", field=models.CharField(blank=True, default="", max_length=255)),
                migrations.AddField(model_name="post", name="image_url", field=models.URLField(blank=True, null=True)),
                migrations.AddField(model_name="post", name="content", field=models.TextField(blank=True, default="")),
                migrations.AddField(model_name="post", name="category", field=models.CharField(choices=[("general", "General"), ("information", "Information"), ("fun", "Fun"), ("technology", "Technology"), ("other", "Other")], default="general", max_length=20)),
            ],
        ),
    ]

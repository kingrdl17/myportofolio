from django.db import migrations, models


def add_project_columns(apps, schema_editor):
    if schema_editor.connection.vendor != "sqlite":
        return
    table = "main_experience"
    with schema_editor.connection.cursor() as cursor:
        cursor.execute('PRAGMA table_info("%s")' % table)
        existing = {row[1] for row in cursor.fetchall()}
        columns = [
            ("project_name", "varchar(255) NOT NULL DEFAULT ''"),
            ("project_description", "text NOT NULL DEFAULT ''"),
            ("technologies_used", "text NOT NULL DEFAULT ''"),
            ("project_link", "varchar(200)"),
        ]
        for name, definition in columns:
            if name not in existing:
                cursor.execute('ALTER TABLE "%s" ADD COLUMN %s %s' % (table, name, definition))


class Migration(migrations.Migration):
    dependencies = [("projects", "0002_project_fields")]
    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                migrations.RunPython(add_project_columns, reverse_code=migrations.RunPython.noop),
            ],
            state_operations=[
                migrations.AddField(model_name="project", name="project_name", field=models.CharField(blank=True, default="", max_length=255)),
                migrations.AddField(model_name="project", name="project_description", field=models.TextField(blank=True, default="")),
                migrations.AddField(model_name="project", name="technologies_used", field=models.TextField(blank=True, default="")),
                migrations.AddField(model_name="project", name="project_link", field=models.URLField(blank=True, null=True)),
            ],
        ),
    ]

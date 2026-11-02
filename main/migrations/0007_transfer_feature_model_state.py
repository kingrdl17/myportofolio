from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0001_adopt_existing_education"),
        ("experience", "0001_adopt_existing_experience"),
        ("main", "0006_experience_starred_by"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(name="Education"),
                migrations.DeleteModel(name="Experience"),
            ],
        ),
    ]

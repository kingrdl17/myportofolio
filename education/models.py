import uuid

from django.db import models


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField()
    ended_at = models.DateField(blank=True, null=True)

    class Meta:
        db_table = "main_education"

    def __str__(self):
        return f"{self.degree} at {self.institution}" if self.degree else self.institution

    @property
    def is_ongoing(self):
        return self.ended_at is None

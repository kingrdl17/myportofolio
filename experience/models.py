import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    PROJECT_CATEGORY_CHOICES = [
        ("web development", "Web Development"),
        ("mobile development", "Mobile Development"),
        ("machine learning", "Machine Learning"),
        ("data science", "Data Science"),
        ("other", "Other"),
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=255, blank=True, default="")
    project_description = models.TextField(blank=True, default="")
    category = models.CharField(
        max_length=30, choices=PROJECT_CATEGORY_CHOICES, default="other"
    )
    technologies_used = models.TextField(blank=True, default="")
    project_link = models.URLField(blank=True, null=True)

    # Legacy columns retained for database compatibility.
    title = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField(blank=True, default="")
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User,
        through="ProjectStar",
        through_fields=("project", "user"),
        related_name="starred_projects",
        blank=True,
    )

    class Meta:
        db_table = "main_experience"

    def __str__(self):
        return self.project_name or self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None


class ProjectStar(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        db_column="experience_id",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
    )

    class Meta:
        db_table = "main_experience_starred_by"
        unique_together = ("project", "user")


Experience = Project

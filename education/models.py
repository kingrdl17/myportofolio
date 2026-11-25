import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    POST_CATEGORY_CHOICES = [
        ("general", "General"),
        ("information", "Information"),
        ("fun", "Fun"),
        ("technology", "Technology"),
        ("other", "Other"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True, default="")
    image_url = models.URLField(blank=True, null=True)
    content = models.TextField(blank=True, default="")
    category = models.CharField(
        max_length=20, choices=POST_CATEGORY_CHOICES, default="general"
    )

    # Legacy columns retained for database compatibility.
    institution = models.CharField(max_length=255, blank=True, default="")
    degree = models.CharField(max_length=255, blank=True, null=True)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateField(default=timezone.now)
    ended_at = models.DateField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User,
        through="PostStar",
        through_fields=("post", "user"),
        related_name="starred_posts",
        blank=True,
    )

    class Meta:
        db_table = "main_education"

    def __str__(self):
        return self.title or (
            f"{self.degree} at {self.institution}" if self.degree else self.institution
        )

    @property
    def is_ongoing(self):
        return self.ended_at is None


class PostStar(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        db_column="education_id",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
    )

    class Meta:
        db_table = "main_education_starred_by"
        unique_together = ("post", "user")


Education = Post

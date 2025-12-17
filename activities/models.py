import secrets
from django.db import models
from django.utils import timezone
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "cities"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.state}"

    def get_absolute_url(self):
        return reverse("city_detail", kwargs={"city_slug": self.slug})


class Neighborhood(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="neighborhoods")
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        unique_together = ["city", "slug"]
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.city.name})"

    def get_absolute_url(self):
        return reverse(
            "neighborhood_detail",
            kwargs={"city_slug": self.city.slug, "neighborhood_slug": self.slug}
        )


class Activity(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    title = models.CharField(max_length=200)
    description = models.TextField()
    neighborhood = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, related_name="activities"
    )
    location_hint = models.CharField(
        max_length=200,
        help_text="Cross streets or landmark (e.g., 'Near 12th & Chicon')"
    )
    starts_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=120)
    helpers_needed = models.PositiveIntegerField(default=1)
    helpers_joined = models.PositiveIntegerField(default=0)
    host_email = models.EmailField()
    host_phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )
    secret_token = models.CharField(max_length=64, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "activities"
        ordering = ["starts_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.secret_token:
            self.secret_token = secrets.token_urlsafe(32)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("activity_detail", kwargs={"pk": self.pk})

    def get_manage_url(self):
        return reverse("activity_manage", kwargs={"token": self.secret_token})

    @property
    def is_happening_now(self):
        now = timezone.now()
        end_time = self.starts_at + timezone.timedelta(minutes=self.duration_minutes)
        return self.starts_at <= now <= end_time

    @property
    def is_upcoming(self):
        return self.starts_at > timezone.now()

    @property
    def is_past(self):
        end_time = self.starts_at + timezone.timedelta(minutes=self.duration_minutes)
        return end_time < timezone.now()

    @property
    def helpers_remaining(self):
        return max(0, self.helpers_needed - self.helpers_joined)

    @property
    def time_display(self):
        now = timezone.now()
        if self.is_happening_now:
            return "Happening now"
        elif self.starts_at.date() == now.date():
            return f"Today at {self.starts_at.strftime('%-I:%M %p')}"
        elif self.starts_at.date() == (now + timezone.timedelta(days=1)).date():
            return f"Tomorrow at {self.starts_at.strftime('%-I:%M %p')}"
        else:
            return self.starts_at.strftime("%a, %b %-d at %-I:%M %p")

    @property
    def duration_display(self):
        hours = self.duration_minutes // 60
        mins = self.duration_minutes % 60
        if hours and mins:
            return f"About {hours}h {mins}m"
        elif hours:
            return f"About {hours} hour{'s' if hours > 1 else ''}"
        else:
            return f"About {mins} minutes"


class ActivityJoin(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="joins"
    )
    session_key = models.CharField(max_length=40)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["activity", "session_key"]

    def __str__(self):
        return f"Join for {self.activity.title}"

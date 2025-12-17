from django.contrib import admin
from .models import City, Neighborhood, Activity, ActivityJoin


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "state", "slug"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "state"]


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ["name", "city", "slug"]
    list_filter = ["city"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "city__name"]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ["title", "neighborhood", "starts_at", "status", "helpers_joined", "helpers_needed"]
    list_filter = ["status", "neighborhood__city", "starts_at"]
    search_fields = ["title", "description", "location_hint"]
    readonly_fields = ["secret_token", "created_at", "updated_at"]
    date_hierarchy = "starts_at"


@admin.register(ActivityJoin)
class ActivityJoinAdmin(admin.ModelAdmin):
    list_display = ["activity", "session_key", "joined_at"]
    list_filter = ["joined_at"]

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from datetime import timedelta

from .models import City, Neighborhood, Activity, ActivityJoin
from .forms import ActivityForm


def home(request):
    cities = City.objects.annotate(
        activity_count=Count(
            "neighborhoods__activities",
            filter=Q(
                neighborhoods__activities__status=Activity.Status.ACTIVE,
                neighborhoods__activities__starts_at__gte=timezone.now() - timedelta(hours=2)
            )
        )
    )
    return render(request, "home.html", {"cities": cities})


def city_detail(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    time_filter = request.GET.get("filter", "today")

    now = timezone.now()
    base_query = Q(
        activities__status=Activity.Status.ACTIVE,
    )

    if time_filter == "now":
        base_query &= Q(
            activities__starts_at__lte=now,
            activities__starts_at__gte=now - timedelta(hours=4)
        )
    elif time_filter == "week":
        base_query &= Q(
            activities__starts_at__gte=now - timedelta(hours=2),
            activities__starts_at__lte=now + timedelta(days=7)
        )
    else:
        end_of_day = now.replace(hour=23, minute=59, second=59)
        base_query &= Q(
            activities__starts_at__gte=now - timedelta(hours=2),
            activities__starts_at__lte=end_of_day
        )

    neighborhoods = city.neighborhoods.annotate(
        activity_count=Count("activities", filter=base_query)
    ).filter(activity_count__gt=0)

    return render(request, "activities/city.html", {
        "city": city,
        "neighborhoods": neighborhoods,
        "time_filter": time_filter,
    })


def neighborhood_detail(request, city_slug, neighborhood_slug):
    neighborhood = get_object_or_404(
        Neighborhood,
        slug=neighborhood_slug,
        city__slug=city_slug
    )
    time_filter = request.GET.get("filter", "today")

    now = timezone.now()
    activities = neighborhood.activities.filter(status=Activity.Status.ACTIVE)

    if time_filter == "now":
        activities = activities.filter(
            starts_at__lte=now,
            starts_at__gte=now - timedelta(hours=4)
        )
    elif time_filter == "week":
        activities = activities.filter(
            starts_at__gte=now - timedelta(hours=2),
            starts_at__lte=now + timedelta(days=7)
        )
    else:
        end_of_day = now.replace(hour=23, minute=59, second=59)
        activities = activities.filter(
            starts_at__gte=now - timedelta(hours=2),
            starts_at__lte=end_of_day
        )

    return render(request, "activities/neighborhood.html", {
        "neighborhood": neighborhood,
        "activities": activities,
        "time_filter": time_filter,
    })


def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    has_joined = ActivityJoin.objects.filter(
        activity=activity,
        session_key=session_key
    ).exists()

    return render(request, "activities/detail.html", {
        "activity": activity,
        "has_joined": has_joined,
    })


@require_POST
def activity_join(request, pk):
    activity = get_object_or_404(Activity, pk=pk)

    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key

    join, created = ActivityJoin.objects.get_or_create(
        activity=activity,
        session_key=session_key
    )

    if created:
        activity.helpers_joined += 1
        activity.save(update_fields=["helpers_joined"])

    if request.htmx:
        return render(request, "components/join_button.html", {
            "activity": activity,
            "has_joined": True,
        })

    return redirect(activity.get_absolute_url())


def activity_directions(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    query = f"{activity.location_hint}, {activity.neighborhood.name}, {activity.neighborhood.city.name}, {activity.neighborhood.city.state}"
    maps_url = f"https://www.google.com/maps/search/?api=1&query={query}"
    return redirect(maps_url)


def activity_post(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return render(request, "activities/post_success.html", {
                "activity": activity,
            })
    else:
        form = ActivityForm()

    cities = City.objects.prefetch_related("neighborhoods")
    return render(request, "activities/post.html", {
        "form": form,
        "cities": cities,
    })


def activity_manage(request, token):
    activity = get_object_or_404(Activity, secret_token=token)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "complete":
            activity.status = Activity.Status.COMPLETED
            activity.save(update_fields=["status"])
        elif action == "cancel":
            activity.status = Activity.Status.CANCELLED
            activity.save(update_fields=["status"])
        elif action == "update":
            form = ActivityForm(request.POST, instance=activity)
            if form.is_valid():
                form.save()

        return redirect(activity.get_manage_url())

    form = ActivityForm(instance=activity)
    return render(request, "activities/manage.html", {
        "activity": activity,
        "form": form,
    })


def search_locations(request):
    query = request.GET.get("q", "").strip()

    if len(query) < 2:
        return render(request, "components/search_results.html", {
            "query": query,
            "cities": [],
            "neighborhoods": [],
            "show_empty": False,
        })

    now = timezone.now()

    cities = City.objects.filter(
        Q(name__icontains=query) | Q(state__icontains=query)
    ).annotate(
        activity_count=Count(
            "neighborhoods__activities",
            filter=Q(
                neighborhoods__activities__status=Activity.Status.ACTIVE,
                neighborhoods__activities__starts_at__gte=now - timedelta(hours=2)
            )
        )
    ).order_by("-activity_count", "name")[:10]

    neighborhoods = Neighborhood.objects.filter(
        name__icontains=query
    ).select_related("city").annotate(
        activity_count=Count(
            "activities",
            filter=Q(
                activities__status=Activity.Status.ACTIVE,
                activities__starts_at__gte=now - timedelta(hours=2)
            )
        )
    ).order_by("-activity_count", "name")[:15]

    return render(request, "components/search_results.html", {
        "query": query,
        "cities": cities,
        "neighborhoods": neighborhoods,
        "show_empty": True,
    })

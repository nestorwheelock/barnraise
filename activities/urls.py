from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search_locations, name="search_locations"),
    path("post/", views.activity_post, name="activity_post"),
    path("activity/<int:pk>/", views.activity_detail, name="activity_detail"),
    path("activity/<int:pk>/join/", views.activity_join, name="activity_join"),
    path("activity/<int:pk>/directions/", views.activity_directions, name="activity_directions"),
    path("manage/<str:token>/", views.activity_manage, name="activity_manage"),
    path("<slug:city_slug>/", views.city_detail, name="city_detail"),
    path("<slug:city_slug>/<slug:neighborhood_slug>/", views.neighborhood_detail, name="neighborhood_detail"),
]

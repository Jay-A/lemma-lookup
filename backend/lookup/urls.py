from django.urls import path

from . import views


urlpatterns = [
    path("lookup/", views.lookup, name="lookup"),
    path("health/", views.health, name="health"),
]



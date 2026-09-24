from django.urls import include, path

urlpatterns = [
    path("", include("apps.website.urls")),
]

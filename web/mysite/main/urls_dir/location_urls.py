from django.urls import path
from main.views_dir.location import LocationCreateView, LocationListView

urlpatterns = [
    path("create/", LocationCreateView.as_view(), name="location_create"),
    path("list/", LocationListView.as_view(), name="location_list"),

]
from django.urls import path
from main.views_dir.location import LocationCreateView, LocationListView, LocationDeleteView, LocationEdit

urlpatterns = [
    path("create/", LocationCreateView.as_view(), name="location_create"),
    path("list/", LocationListView.as_view(), name="location_list"),
    path("edit/<int:pk>", LocationEdit.as_view(), name="location_edit"),
    path("delete/<int:pk>", LocationDeleteView.as_view(), name="location_delete"),

]
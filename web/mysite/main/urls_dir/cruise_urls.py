from django.urls import path
from main.views_dir.cruise import CruiseCreateView, CruiseDetailView, CruiseUpdateView, CruiseListView, CruiseDeleteView

urlpatterns = [
    path("create/", CruiseCreateView.as_view(), name="cruise_create"),
    path("edit/<int:pk>", CruiseUpdateView.as_view(), name="cruise_edit"),
    path("details/<int:pk>", CruiseDetailView.as_view(), name="cruise_details"),
    path("delete/<int:pk>", CruiseDeleteView.as_view(), name="cruise_delete"),
    path("list/", CruiseListView.as_view(), name="cruise_list"),
]
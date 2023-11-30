from django.urls import path
from main.views_dir.cruise import CruiseCreateView, CruiseDetailView, CruiseUpdateView, CruiseListView

urlpatterns = [
    path("create/", CruiseCreateView.as_view(), name="cruise_create"),
    path("edit/<int:pk>", CruiseUpdateView.as_view(), name="cruise_edit"),
    path("details/<int:pk>", CruiseDetailView.as_view(), name="cruise_details"),
    path("list/", CruiseListView.as_view(), name="cruise_list"),
]
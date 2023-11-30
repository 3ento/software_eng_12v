from django.urls import path
from main.views_dir.captains import CaptainCreateView, CaptainListView, CaptainEdit, CaptainDeleteView

urlpatterns = [
    path("create/", CaptainCreateView.as_view(), name="captain_create"),
    path("list/", CaptainListView.as_view(), name="captain_list"),
    path("edit/<int:pk>", CaptainEdit.as_view(), name="captain_edit"),
    path("delete/<int:pk>", CaptainDeleteView.as_view(), name="captain_delete"),

]
from django.urls import path
from main.views_dir.captains import CaptainCreateView, CaptainListView

urlpatterns = [
    path("create/", CaptainCreateView.as_view(), name="captain_create"),
    path("list/", CaptainListView.as_view(), name="captain_list"),

]
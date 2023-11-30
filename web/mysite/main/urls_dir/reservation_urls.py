from django.urls import path
from main.views_dir.reservation import ReservationCreateView, ReservationListView

urlpatterns = [
    path("create/", ReservationCreateView.as_view(), name="reserve"),
    path("list/", ReservationListView.as_view(), name="reservation_list"),
]
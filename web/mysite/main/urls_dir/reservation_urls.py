from django.urls import path
from main.views_dir.reservation import ReservationCreateView, ReservationListView, ReservationUpdateView

urlpatterns = [
    path("create/<int:pk>", ReservationCreateView.as_view(), name="reserve"),
    path("list/", ReservationListView.as_view(), name="reservation_list"),
    path("edit/<int:pk>",  ReservationUpdateView.as_view() ,name="reservation_edit")
]   
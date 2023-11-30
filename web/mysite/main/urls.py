from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("cruise_create/", views.CruiseCreateView.as_view(), name="cruise_create"),
    path("cruise_edit/<int:pk>", views.CruiseUpdateView.as_view(), name="cruise_edit"),
    path("cruise_details/<int:pk>", views.CruiseDetailView.as_view(), name="cruise_details"),
    path("cruises/", views.CruiseListView.as_view(), name="cruise_list"),

    path("captain_create/", views.CaptainCreateView.as_view(), name="captain_create"),
    path("captains/", views.CaptainListView.as_view(), name="captain_list"),

    path("location_create/", views.LocationCreateView.as_view(), name="location_create"),
    path("locations/", views.LocationListView.as_view(), name="location_list"),

    path("reserve/", views.ReservationCreateView.as_view(), name="reserve"),
    path("reservation_list", views.ReservationListView.as_view(), name="reservation_list"),

    path("profile_create/", views.ProfileCreate.as_view(), name="profile_create"),
    path("log_in/", views.UserLoginView.as_view(), name="log in"),
    path("logout/", views.LogoutView.as_view(next_page="home"), name="logout")
]
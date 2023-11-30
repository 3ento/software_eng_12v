from django.urls import path
from main.views_dir.profile import ProfileCreate, ProfileLogOut, UserLoginView

urlpatterns = [
    path("profile_create/", ProfileCreate.as_view(), name="profile_create"),
    path("log_in/", UserLoginView.as_view(), name="log in"),
    path("logout/", ProfileLogOut.as_view(next_page="home"), name="logout")
]
from typing import Any
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView
from main.models import Cruise, CruiseLocation, Captain, Reservation, SeaManagerCruiseUser
from main.forms import CreateCruise, CreateCaptain, CreateLocation, CreateUserForm, ReservationCreateForm

# Locations
class LocationCreateView(CreateView):
    model = CruiseLocation
    form_model = CreateLocation
    template_name = "./location_views/location_create.html"
    fields = '__all__'

    success_url = reverse_lazy("home")

class LocationListView(ListView):
    model = CruiseLocation
    template_name = "./location_views/location_list.html"
    context_object_name = 'locations'
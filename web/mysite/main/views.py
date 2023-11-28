from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, ListView
from main.models import Cruise, CruiseLocation, Captain
from main.forms import CreateCruise, CreateCaptain, CreateLocation

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

# Cruises
class CruiseCreateView(CreateView):
    model = Cruise
    form_model = CreateCruise
    template_name = "cruise_create.html"
    fields = "__all__"

    success_url = reverse_lazy("home")

class CruiseListView(ListView):
    model = Cruise
    template_name = "cruise_list.html"
    context_object_name = 'cruises'

# Captains
class CaptainCreateView(CreateView):
    model = Captain
    form_model = CreateCaptain
    template_name = "captain_create.html"
    fields = '__all__'

    success_url = reverse_lazy("home")

class CaptainListView(ListView):
    model = Captain
    template_name = "captain_list.html"
    context_object_name = 'captains'


# Locations
class LocationCreateView(CreateView):
    model = CruiseLocation
    form_model = CreateLocation
    template_name = "location_create.html"
    fields = '__all__'

    success_url = reverse_lazy("home")

class LocationListView(ListView):
    model = CruiseLocation
    template_name = "location_list.html"
    context_object_name = 'locations'
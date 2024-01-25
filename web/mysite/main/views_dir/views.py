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

# Create your views here.

class HomeView(ListView):
    model = Cruise
    context_object_name = 'cruises'

    template_name = "home.html"

    
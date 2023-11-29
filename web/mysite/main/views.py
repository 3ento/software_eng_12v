from typing import Any
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, ListView
from main.models import Cruise, CruiseLocation, Captain, Reservation, SeaManagerCruiseUser
from main.forms import CreateCruise, CreateCaptain, CreateLocation, CreateUserForm, ReservationCreateForm

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


# Reservations
class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "reservation_create.html"
    fields = '__all__'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation_list.html'
    context_object_name = 'reservations'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # context["reservee_name"] = SeaManagerCruiseUser.objects.get(pk=self.object.cruise_reservee)
        
        return super().get_context_data(**kwargs)

# Users
class ProfileCreate(CreateView):
    form_class = CreateUserForm
    template_name = 'profile_create.html'
    success_url = reverse_lazy('home')

    
    #def form_valid(self, *args, **kwargs):
     #   result = super().form_valid(*args, **kwargs)
      #  login(self.request, self.object)

 #       return result

class UserLoginView(LoginView):
    template_name = 'login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return super().get_success_url()
        

class ProfileLogOut(LogoutView):
    next_page = reverse_lazy('home')
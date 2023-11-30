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

class HomeView(TemplateView):
    template_name = "home.html"

# Cruises
class CruiseCreateView(CreateView):
    model = Cruise
    form_model = CreateCruise
    template_name = "./cruise_views/cruise_create.html"
    fields = "__all__"

    success_url = reverse_lazy("cruise_list")

class CruiseUpdateView(UpdateView):
    model = Cruise
    template_name = "./cruise_views/cruise_edit.html"
    fields = "__all__"

    success_url = reverse_lazy("cruise_list")

class CruiseDetailView(DetailView):
    model = Cruise
    template_name = "./cruise_views/cruise_details.html"
    context_object_name = 'cruise'    

    def get_context_data(self, **kwargs):
        cruise = Cruise.objects.filter(id=self.object.id)
        ctx = super().get_context_data(**kwargs)

        ctx.update({
            'econ_cc': cruise[0].econ_total_capacity - len(Reservation.objects.filter(cruise_id=self.object.id).filter(ticket_type="Economy")),
            'bus_cc': cruise[0].business_total_capacity - len(Reservation.objects.filter(cruise_id=self.object.id).filter(ticket_type="Business")),
        })

        return ctx

class CruiseListView(ListView):
    model = Cruise
    template_name = "./cruise_views/cruise_list.html"
    context_object_name = 'cruises'

# Captains
class CaptainCreateView(CreateView):
    model = Captain
    form_model = CreateCaptain
    template_name = "./captain_views/captain_create.html"
    fields = '__all__'

    success_url = reverse_lazy("home")

class CaptainListView(ListView):
    model = Captain
    template_name = "./captain_views/captain_list.html"
    context_object_name = 'captains'


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


# Reservations
class ReservationCreateView(CreateView):
    model = Reservation
    template_name = "./reservation_views/reservation_create.html"
    fields = '__all__'

    def form_valid(self, form):
        form.instance.cruise_reservee = self.request.user
        form.save()

        return super().form_valid(form)

    success_url = reverse_lazy('home')

class ReservationListView(ListView):
    model = Reservation
    template_name = './reservation_views/reservation_list.html'
    context_object_name = 'reservations'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # context["reservee_name"] = SeaManagerCruiseUser.objects.get(pk=self.object.cruise_reservee)
        
        return super().get_context_data(**kwargs)

# Users
class ProfileCreate(FormView):
    template_name = './profile_views/profile_create.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        
        return super(ProfileCreate, self).form_valid(form)
 
class UserLoginView(LoginView):
    template_name = './profile_views/login_page.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return super().get_success_url()
        

class ProfileLogOut(LogoutView):
    next_page = reverse_lazy('home')
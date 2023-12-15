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
from django.contrib.auth.mixins import LoginRequiredMixin


# Reservations
class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    template_name = "./reservation_views/reservation_create.html"
    fields = ('ticket_type', 'number_of_tickets')
    context_object_name = 'reservation'

    def form_valid(self, form):
        form.instance.cruise_reservee_id = self.request.user.id
        form.instance.cruise = Cruise.objects.get(id=self.kwargs['pk'])

        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context.update({
        })

        return super().get_context_data(**kwargs)


    success_url = reverse_lazy('home')

class ReservationListView(ListView):
    model = Reservation
    template_name = './reservation_views/reservation_list.html'
    context_object_name = 'reservations'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # context["reservee_name"] = SeaManagerCruiseUser.objects.get(pk=self.object.cruise_reservee)
        
        return super().get_context_data(**kwargs)
    

class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    template_name = "./cruise_views/reservation_edit.html"
    fields = ('cruise', 'ticket_type', 'number_of_tickets')

    def form_valid(self, form):
        form.instance.cruise_reservee_id = self.request.user.id

        return super().form_valid(form)

    success_url = reverse_lazy("home")
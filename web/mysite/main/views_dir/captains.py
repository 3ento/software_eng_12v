from typing import Any
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import FormView, CreateView, DetailView, ListView, UpdateView, DeleteView
from main.models import Cruise, CruiseLocation, Captain, Reservation, SeaManagerCruiseUser
from main.forms import CreateCruise, CreateCaptain, CreateLocation, CreateUserForm, ReservationCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Captains
class CaptainCreateView(LoginRequiredMixin, CreateView):
    model = Captain
    form_model = CreateCaptain
    template_name = "./captain_views/captain_create.html"
    fields = '__all__'

    success_url = reverse_lazy("home")

class CaptainListView(ListView):
    model = Captain
    template_name = "./captain_views/captain_list.html"
    context_object_name = 'captains'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        cruise = Cruise.objects.all()

        def get_current_captains_cruises(curr_captain_id):
            return cruise.filter(captain_name_id=curr_captain_id)

        for el in self.object_list:
            el.curr_cruises = get_current_captains_cruises(el.id)

        return context

class CaptainEdit(LoginRequiredMixin, UpdateView):
    model = Captain
    template_name = "./captain_views/captain_edit.html"
    fields = '__all__'

    success_url = reverse_lazy("captain_list")

class CaptainDeleteView(LoginRequiredMixin, DeleteView):
    model = Captain
    template_name = './captain_views/captain_delete.html'
    context_object_name = 'captain'

    def get_success_url(self):
        return reverse_lazy('captain_list')
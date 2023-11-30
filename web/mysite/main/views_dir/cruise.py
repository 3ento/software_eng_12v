from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from main.models import Cruise, Reservation
from main.forms import CreateCruise
from django.urls import reverse_lazy


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

class CruiseDeleteView(DeleteView):
    model = Cruise
    template_name = './cruise_views/cruise_delete.html'
    context_object_name = 'cruise'

    def get_success_url(self):
        return reverse_lazy('cruise_list')
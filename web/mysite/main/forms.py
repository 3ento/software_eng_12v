from django.forms import ModelForm
from main.models import Cruise, CruiseLocation, Captain, SeaManagerCruiseUser, Reservation
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CreateCruise(forms.Form):
    class Meta:
        model = Cruise  
        fields = '__all__'


class CreateCaptain(ModelForm):
    class Meta:
        model = Captain
        fields = '__all__'


class CreateLocation(ModelForm):
    class Meta:
        model = CruiseLocation
        fields = '__all__'


class CreateUserForm(ModelForm):
    class Meta:
        model = SeaManagerCruiseUser
        exclude = ('last_login',)


class ReservationCreateForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ("cruise_reservee",)
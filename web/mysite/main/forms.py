from django.forms import ModelForm
from main.models import Cruise, CruiseLocation, Captain
from django import forms

class CreateCruise(ModelForm):
    class Meta:
        model = Cruise
        fields = '__all__'

        widgets = {
            'departure_date_time':forms.TextInput(attrs={'type':'datetime-local'}),
            'arrival_date_time':forms.TextInput(attrs={'type':'datetime-local'}),
        }

class CreateCaptain(ModelForm):
    class Meta:
        model = Captain
        fields = '__all__'

class CreateLocation(ModelForm):
    class Meta:
        model = CruiseLocation
        fields = '__all__'
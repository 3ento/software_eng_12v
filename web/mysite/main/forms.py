from django.forms import ModelForm
from main.models import Cruise, CruiseLocation, Captain, SeaManagerCruiseUser
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


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


class CreateUserForm(BootstrapFormMixin, UserCreationForm):
    username = forms.CharField(
        max_length=30,
    )

    USERNAME_FIELD = 'username'

    name = forms.CharField(
        max_length=30
    )

    surname = forms.CharField(
        max_length=30,
        required=False,
    )

    email = forms.EmailField(
    )

    EGN = forms.CharField(
        max_length=10
    )

    address = forms.CharField(
        max_length=30
    )

    phone_number = forms.CharField(
        max_length=15,
        required=False,
    )

    is_staff = forms.BooleanField(
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = SeaManagerCruiseUser(
            username=self.cleaned_data['username'],
            name=self.cleaned_data['name'],
            surname=self.cleaned_data['surname'],
            email=self.cleaned_data['email'],
            EGN=self.cleaned_data['EGN'],
            address=self.cleaned_data['address'],
            phone_number=self.cleaned_data['phone_number'],
            is_staff=self.cleaned_data['is_staff'],
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = SeaManagerCruiseUser
        fields = '__all__'
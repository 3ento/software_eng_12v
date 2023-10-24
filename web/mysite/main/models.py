from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
from main.managers import AppUserManager


class AppUser(User):
    name = models.CharField(
        max_length=30
    )

    surname = models.CharField(
        max_length=30
    )

    EGN = models.CharField(
        max_length=10
    )

    address = models.CharField(
        max_length=30
    )

    phone_number = models.CharField(
        max_length=15
    )


class Cruise(models.Model):
    # TODO:
    #  1. make from-to location a choice field from all possible locations cruises go (i.e make a cruise_locations model)
    #  2. make captains a choice from a Captains model

    CRUISE_TYPES = [
        ("Week-long", "Week-long"),
        ("Day-long", "Day-long")
    ]

    from_location = models.CharField(
        max_length=50
    )
    to_location = models.CharField(
        max_length=50
    )

    departure_date_time = models.DateTimeField()
    arrival_date_time = models.DateTimeField()

    type = models.CharField(
        max_length=9,
        choices=CRUISE_TYPES
    )

    unique_cruise_number = models.IntegerField(
        unique=True
    )

    captain_name = models.CharField(
        max_length=50
    )

    econ_total_capacity = models.IntegerField()
    business_total_capacity = models.IntegerField()

    econ_free_spaces_left = 0
    business_free_spaces_left = 0


class Reservations(models.Model):
    TICKET_TYPES = [
        ("Economy", "Economy"),
        ("Business", "Business")
    ]

    cruise_number = models.ForeignKey(Cruise, on_delete=models.CASCADE)

    # note: питай Стойчев да го променим това на one-to-many връзка вместо отделни колони
    # name = 0
    # middle_name = 0
    # surname = 0
    # EGN = 0
    # phone_number = 0
    # nationality = 0

    ticket_type = models.CharField(
        max_length=8,
        choices=TICKET_TYPES
    )

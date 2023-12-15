from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from main.managers import AppUserManager


class SeaManagerCruiseUser(AbstractBaseUser):

    username = models.CharField(
        max_length=30,
        unique=True
    )

    USERNAME_FIELD = 'username'

    name = models.CharField(
        max_length=30
    )

    surname = models.CharField(
        max_length=30
    )

    email = models.EmailField(
        default='email@example.com'
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

    is_staff = models.BooleanField(
        default=False,
        blank=True,
    )

    objects = AppUserManager()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Captain(models.Model):

    name = models.CharField(
        max_length=30
    )
    surname = models.CharField(
        max_length=30
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class CruiseLocation(models.Model):

    name = models.CharField(null=True, blank=True, max_length=15)

    def __str__(self):
        return self.name


class Cruise(models.Model):

    CRUISE_TYPES = [
        ("Week-long", "Week-long"),
        ("Day-long", "Day-long")
    ]

    from_location = models.ForeignKey(CruiseLocation, related_name="from-location+", on_delete=models.CASCADE)
    to_location = models.ForeignKey(CruiseLocation, related_name="to-location+", on_delete=models.CASCADE)

    departure_date_time = models.DateTimeField()

    type = models.CharField(
        max_length=9,
        choices=CRUISE_TYPES
    )

    captain_name = models.ForeignKey(Captain, on_delete=models.CASCADE)

    econ_total_capacity = models.IntegerField()
    business_total_capacity = models.IntegerField()

    def __str__(self):
        return f'{self.type} cruise: {self.from_location} - {self.to_location}'

class Reservation(models.Model):
    TICKET_TYPES = [
        ("Economy", "Economy"),
        ("Business", "Business")
    ]

    cruise = models.ForeignKey(Cruise, on_delete=models.CASCADE)

    cruise_reservee = models.ForeignKey(SeaManagerCruiseUser, on_delete=models.CASCADE)

    ticket_type = models.CharField(
        max_length=8,
        choices=TICKET_TYPES
    )

    number_of_tickets = models.IntegerField(default=1, blank=False, null=False)

    def __str__(self):
        return f'{self.number_of_tickets} reservation(s) for {self.cruise}, by {self.cruise_reservee}'
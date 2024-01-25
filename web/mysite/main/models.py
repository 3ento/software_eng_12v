from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from main.managers import AppUserManager


class SeaManagerCruiseUser(AbstractBaseUser, PermissionsMixin):

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

    profile_picture = models.URLField(
        default='https://gcaptain.com/wp-content/uploads/2017/07/grumpy-ship-captain.jpeg'
    )

    def __str__(self):
        return f'{self.name} {self.surname}'


class CruiseLocation(models.Model):

    name = models.CharField(null=True, blank=True, max_length=15)
    image = models.URLField(default='https://www.planetware.com/wpimages/2021/10/best-tropical-vacations-mauritius-aerial.jpg')
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cruise(models.Model):

    CRUISE_TYPES = [
        ("Week-long", "Week-long"),
        ("Day-long", "Day-long")
    ]

    from_location = models.ForeignKey(CruiseLocation, related_name="from-location+", on_delete=models.CASCADE)
    to_location = models.ForeignKey(CruiseLocation, related_name="to-location+", on_delete=models.CASCADE)

    type = models.CharField(
        max_length=9,
        choices=CRUISE_TYPES
    )

    captain_name = models.ForeignKey(Captain, on_delete=models.CASCADE)

    departure_date_time = models.DateTimeField()

    econ_total_capacity = models.IntegerField()
    business_total_capacity = models.IntegerField()

    image_main = models.URLField(default='https://images.pexels.com/photos/813011/pexels-photo-813011.jpeg')
    image_1 = models.URLField(default='https://media.istockphoto.com/id/458115989/photo/cruise-ship-in-caribbean-sea.jpg?s=612x612&w=0&k=20&c=wMweujKOnZOpihjorKHEdgqI-LDMJkLF-LpV_FhtUWE=')
    image_2 = models.URLField(default='https://media.istockphoto.com/id/1222173565/photo/cruise-ship-msc-seaside-at-cozumel-island-mexico.jpg?s=612x612&w=0&k=20&c=2w3dQqb196mclsS-oMbFEgYl3r7jgQZFgvKYdASUEMs=')
    image_3 = models.URLField(default='https://media.istockphoto.com/id/516463721/photo/3d-cruise-ship-in-beautiful-ocean-with-blue-sky.jpg?s=612x612&w=0&k=20&c=97aWdauUuFSZwMXZ6Ky4TZDuxg9vhjDb98wFj0vwL3s=')
    image_4 = models.URLField(default='https://media.istockphoto.com/id/1155311911/photo/luxury-cruise-ship-sailing-from-the-port-at-sunrise-across-the-ocean-beautiful-summer.jpg?s=612x612&w=0&k=20&c=im3OvbdWWN-vdwcVcSFMGKpmpbB97Elj5Nva8UXJlmA=')

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
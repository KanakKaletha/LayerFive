from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('DLX', 'Deluxe'),
        ('SMD', 'Semi Deluxe'),
        ('NRM', 'Normal')
    )
    room_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    available = models.BooleanField(default=True)

    @classmethod
    def room_count_available(cls):
        return cls.objects.filter(available=True).count()

class Booking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

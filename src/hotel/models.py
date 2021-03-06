from django.db import models

from datetime import datetime 

class Room(models.Model):
    bed_type = models.CharField(max_length=20)
    facilities = models.TextField(null=True)
    price = models.FloatField(default=0)
    last_modified = models.DateTimeField(null=False, default=datetime.now())

    def __str__(self):
        return("ID:#{} {}".format(self.id, self.bed_type))

class Booking(models.Model):
    customer_full_name = models.CharField(max_length=100)
    start_datetime = models.DateField(null=False, default=datetime.now())
    end_datetime = models.DateField(null=False, default=datetime.now())
    last_modified = models.DateTimeField(null=False, default=datetime.now())
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')

    def __str__(self):
        return("#{} {}".format(self.id, self.room))

class Checkin(models.Model):
    customer_full_name = models.CharField(max_length=100)
    start_datetime = models.DateField(null=False, default=datetime.now())
    end_datetime = models.DateField(null=False, default=datetime.now())
    last_modified = models.DateTimeField(null=False, default=datetime.now())
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='checkins')

    def __str__(self):
        return("#{} {}".format(self.id, self.room))

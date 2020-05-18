from django.db import models


class Room(models.Model):
    bad_type = models.CharField(max_length=20)


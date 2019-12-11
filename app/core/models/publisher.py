from django.db import models
from .timestamp import TimeStampModel

class Publisher(TimeStampModel, models.Model):
    """ Model for Publisher """
    name = models.CharField(max_length=250)

    def __str__(self):
        """ String rep for Publisher """
        return self.name

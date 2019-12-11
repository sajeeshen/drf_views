from django.db import models


class TimeStampModel(models.Model):
    """ Generic model class for all the time stamp related """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


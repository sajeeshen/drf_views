from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        """ String rep for Author model """
        return self.name
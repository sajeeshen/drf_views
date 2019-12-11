from django.db import models


class Author(models.Model):
    name = models.CharField(default=None, max_length=250)
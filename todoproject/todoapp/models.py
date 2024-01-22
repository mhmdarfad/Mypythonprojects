from django.db import models
from django.db.models import IntegerField


# Create your models here.
class Task(models.Model):

    name = models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name

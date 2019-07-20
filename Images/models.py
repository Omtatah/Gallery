import datetime as dt
from django.db import models
# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

    @classmethod
    def delete_category(cls,name):
        cls.objects.filter(name = name).delete()
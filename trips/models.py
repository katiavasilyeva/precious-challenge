# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# A Service can be an Activity, Transport or Accommodation
# A service can belong to multiple trips and trips can have multiple services (many-to-many)
# Services have a service date, service type, service name and cost.
class Service(models.Model):
    name = models.CharField(max_length=300,default="Service",unique=True)
    type_choices = (("ACN","Accommodation"),
        ("TRA", "Transportation"),
        ("ACT", "Activity"))
    date = models.DateField()
    type = models.CharField(max_length=100,choices=(type_choices))
    cost = models.IntegerField(default=0)

    def __str__(self):
        # ensure that the service shows up by its name in the admin tool
        return self.name

class Trip(models.Model):
    # title_field contains the trip name
    title = models.CharField(max_length=300,unique=True)
    # travel_style field contains the type of G Adventures Trip
    travel_style = models.CharField(max_length=300)
    # destination contains the country in which the trip takes place
    destination = models.CharField(max_length=300)
    # duration_days details how long the trip is in days
    duration_days = models.IntegerField()
    # the default for a trip cost is 0
    cost = models.IntegerField(default=0)
    # add relationship to service model
    service = models.ManyToManyField(Service)

    # replace cost field with a property
    @property
    def cost(self):
        # the total for the trip is the sum of all the services that it is made up of
        total = sum(service.cost for service in self.service.all())
        # a 10% service charge is taken on top of the trip cost
        service_charge = sum(service.cost for service in self.service.all())*.10
        # return the total which is the base cost plus service charge
        return total + service_charge




import datetime

from django.db import models
from django.utils import timezone


class Property(models.Model):
    property_name = models.CharField(max_length=200)
    property_address = models.CharField(max_length=200)
    property_zip = models.IntegerField(default=0)
    property_state = models.CharField(max_length=200)
    property_city = models.CharField(max_length=200)
    property_price = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    last_price = models.DecimalField(decimal_places=2, max_digits=12)
    volume = models.IntegerField(default=0)
    outstanding_shares = models.IntegerField(default=0.00)
    rent_rate = models.DecimalField(decimal_places=2, max_digits=12)
    total_shares = models.DecimalField(decimal_places=2, max_digits=12)

    @property
    def rent_yield_per_share(self):
        return self.rent_rate / self.total_shares

    @property
    def rent_yield(self):
        result = (self.rent_yield_per_share / self.last_price)*1200
        return float("{0:.2f}".format(result))

    def __str__(self):
        return self.property_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

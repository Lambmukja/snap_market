from django.db import models


# Create your models here.
class Contract(models.Model):
    market_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    consumer_idx = models.PositiveSmallIntegerField(blank=False, null=False)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE


class Competition(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    competition_name = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False, default=str(datetime.now().date()))
    end_date = models.DateField(null=True, blank=True)

class Swimming(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    competition_id = models.ForeignKey(Competition, on_delete=CASCADE, related_name='competition_id')
    athlete = models.CharField(max_length=200, null=False, blank=False)
    value = models.DecimalField(max_digits=6, decimal_places=3)
    unit_measurement = models.CharField(max_length=2)


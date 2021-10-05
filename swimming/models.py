from django.db import models
from django.db.models.deletion import CASCADE


class SwimmingCompetition(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    competition_name = models.CharField(max_length=200, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    results = models.CharField(max_length=20, null=False, blank=False, default="partial_result")

class SwimmingAthletes(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    competition = models.ForeignKey(SwimmingCompetition, on_delete=CASCADE, related_name='competition_id')
    athlete = models.CharField(max_length=200, null=False, blank=False)
    value = models.DecimalField(max_digits=6, decimal_places=3)
    unit_measurement = models.CharField(max_length=2)

    class Meta:
        ordering = ['value']

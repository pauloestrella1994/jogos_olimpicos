from django.db.models import fields
from rest_framework import serializers
from .models import SwimmingAthletes, SwimmingCompetition


class SwimmingAthletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingAthletes
        fields = [
            'id',
            'competition_id',
            'athlete',
            'value',
            'unit_measurement',
        ]


class SwimmingCompetitionSerializer(serializers.ModelSerializer):
    athletes = SwimmingAthletesSerializer(many=True, read_only=True, source='competition_id')

    class Meta:
        model = SwimmingCompetition
        fields = [
            'id',
            'competition_name',
            'start_date',
            'end_date',
            'athletes',
        ]
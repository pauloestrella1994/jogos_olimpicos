from rest_framework import serializers
from .models import DartThrowAthletes, DartThrowCompetition

class DartThrowAthletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DartThrowAthletes
        fields = [
            'id',
            'competition',
            'athlete',
            'value',
            'unit_measurement',
        ]

class DartThrowCompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DartThrowCompetition
        fields = [
            'id',
            'competition_name',
            'start_date',
            'end_date',
            'results',
            'athletes_results',
        ]        

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

    def validate(self, data):
        competition_end_date = data["competition"].end_date
        if competition_end_date:
            raise serializers.ValidationError("The competition is over")
        return data

class DartThrowCompetitionSerializer(serializers.ModelSerializer):
    athletes_results = DartThrowAthletesSerializer(many=True, read_only=True, source='competition_id')
    
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

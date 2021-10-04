from django.db.models import fields
from rest_framework import serializers, validators
from .models import SwimmingAthletes, SwimmingCompetition


class SwimmingAthletesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwimmingAthletes
        validators = [
            validators.UniqueTogetherValidator(
                queryset=SwimmingAthletes.objects.all(),
                fields=["competition", "athlete"]
        )]
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
    
    def validate(self, data):
        start_date = data.get("start_date", self.instance.start_date)
        end_date = data.get("end_date", None)
            
        if start_date > end_date:
            raise serializers.ValidationError("Start date competition can't be later then end date")
        return data
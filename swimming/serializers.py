from django.db import transaction
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
    athletes_results = SwimmingAthletesSerializer(many=True, read_only=True, source='competition_id')

    class Meta:
        model = SwimmingCompetition
        fields = [
            'id',
            'competition_name',
            'start_date',
            'end_date',
            'results',
            'athletes_results',
        ]
    
    def validate(self, data):
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        
        if start_date is None:
            try:
                start_date = self.instance.start_date
            except:
                raise serializers.DjangoValidationError("Competition can't be created without a start date.")

        if end_date is not None and start_date > end_date:
            raise serializers.ValidationError("Start date competition can't be later then end date.")
        
        if end_date:
            with transaction.atomic():
                try:
                    self.instance.results = "competition ended"
                    self.instance.save()
                except:
                    raise serializers.DjangoValidationError("It is not possible to close a competition if there is not yet one.")
        return data
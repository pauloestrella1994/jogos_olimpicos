from django.db import transaction
from rest_framework import serializers, validators
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
        competition = data.get("competition", None)
        athlete = data.get("athlete", None)

        if competition is not None:
            if competition.end_date:
                raise serializers.ValidationError("The competition is over")
            if athlete is not None:
                number_of_marks = DartThrowAthletes.objects.filter(competition=competition.id, athlete=athlete)
                if len(number_of_marks.values()) >= 3:
                    raise serializers.ValidationError("The athlete already has 3 marks in this competition")
        
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


class DartThrowPodiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = DartThrowAthletes
        fields = [
            'id',
            'athlete',
            'value',
            'unit_measurement'
        ]

from django.db.models import fields
from rest_framework import serializers
from .models import Competition, Swimming


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = (
            'id',
            'competition_name',
            'start_date',
            'end_date',
        )


class SwimmingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swimming
        fields = (
            'id',
            'competition_id',
            'athlete',
            'value',
            'unit_measurement',
        )
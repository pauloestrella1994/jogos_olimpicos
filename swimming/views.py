from django.shortcuts import render
from rest_framework import viewsets

from .models import SwimmingCompetition, SwimmingAthletes
from .serializers import SwimmingAthletesSerializer, SwimmingCompetitionSerializer


class SwimmingAthletesViewSet(viewsets.ModelViewSet):
    queryset = SwimmingAthletes.objects.all()
    serializer_class = SwimmingAthletesSerializer

class SwimmingCompetitionViewSet(viewsets.ModelViewSet):
    queryset = SwimmingCompetition.objects.all()
    serializer_class = SwimmingCompetitionSerializer

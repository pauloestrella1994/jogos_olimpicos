from django.shortcuts import render
from rest_framework import viewsets

from .models import DartThrowAthletes, DartThrowCompetition
from .serializers import DartThrowAthletesSerializer, DartThrowCompetitionSerializer


class DartThrowAthletesViewSet(viewsets.ModelViewSet):
    queryset = DartThrowAthletes.objects.all()
    serializer_class = DartThrowAthletesSerializer

class DartThrowCompetitionViewSet(viewsets.ModelViewSet):
    queryset = DartThrowCompetition.objects.all()
    serializer_class = DartThrowCompetitionSerializer

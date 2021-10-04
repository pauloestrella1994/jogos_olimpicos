from django.shortcuts import render
from rest_framework import generics

from .models import SwimmingCompetition, SwimmingAthletes
from .serializers import SwimmingAthletesSerializer, SwimmingCompetitionSerializer


class SwimmingAthletesView(generics.ListCreateAPIView):
    queryset = SwimmingAthletes.objects.all()
    serializer_class = SwimmingAthletesSerializer

class SwimmingCompetitionView(generics.ListCreateAPIView):
    queryset = SwimmingCompetition.objects.all()
    serializer_class = SwimmingCompetitionSerializer


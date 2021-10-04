from django.shortcuts import render
from rest_framework import generics

from .models import Swimming, Competition
from .serializers import CompetitionSerializer, SwimmingSerializer


class SwimmingAthletesView(generics.ListCreateAPIView):
    queryset = Swimming.objects.all()
    serializer_class = SwimmingSerializer

class SwimmingCompetitionView(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer


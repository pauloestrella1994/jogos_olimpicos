from operator import itemgetter
from django.db.models.query import QuerySet
from rest_framework import viewsets, generics
from .models import DartThrowAthletes, DartThrowCompetition
from .serializers import (
    DartThrowAthletesSerializer, 
    DartThrowCompetitionSerializer, 
    DartThrowPodiumSerializer
)


class DartThrowAthletesViewSet(viewsets.ModelViewSet):
    queryset = DartThrowAthletes.objects.all()
    serializer_class = DartThrowAthletesSerializer

class DartThrowCompetitionViewSet(viewsets.ModelViewSet):
    queryset = DartThrowCompetition.objects.all()
    serializer_class = DartThrowCompetitionSerializer

class DartThrowPodiumView(generics.ListAPIView):
    serializer_class = DartThrowPodiumSerializer

    def get_queryset(self):
        competition_id = int(str(self.request)[-4])
        queryset = DartThrowAthletes.objects.filter(
            competition_id=competition_id
            ).values('value', 'athlete', 'unit_measurement').order_by('value')
        data = sorted(list({i['athlete']:i for i in queryset}.values()), key=itemgetter('value'), reverse=True)
        return data

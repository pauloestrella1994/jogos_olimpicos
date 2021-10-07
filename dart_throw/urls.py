from django import urls
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import DartThrowCompetitionViewSet, DartThrowAthletesViewSet, DartThrowPodiumView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dart-throw-athletes', DartThrowAthletesViewSet)
router.register(r'dart-throw-competition', DartThrowCompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dart-throw-podium/<int:competition_id>/', DartThrowPodiumView.as_view(), name='dart_throw_podium')
]
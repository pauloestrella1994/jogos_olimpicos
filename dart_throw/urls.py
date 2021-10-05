from django import urls
from django.urls import path
from django.urls.conf import include
from django.urls.resolvers import URLPattern
from .views import DartThrowCompetitionViewSet, DartThrowAthletesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'dart-throw-athletes', DartThrowAthletesViewSet)
router.register(r'dart-throw-competition', DartThrowCompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from django.urls.conf import include
from .views import SwimmingCompetitionViewSet, SwimmingAthletesViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'swimming-athletes', SwimmingAthletesViewSet)
router.register(r'swimming-competition', SwimmingCompetitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
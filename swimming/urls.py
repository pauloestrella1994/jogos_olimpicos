from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SwimmingCompetitionView, SwimmingAthletesView

urlpatterns = [
    path('swimming-athletes/', SwimmingAthletesView.as_view(), name='swimming_athletes'),
    path('swimming-competition/', SwimmingCompetitionView.as_view(), name='swimming_competition')
]
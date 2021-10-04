from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SwimmingCompetitionView

urlpatterns = [
    path('swimming/', SwimmingCompetitionView.as_view(), name='swimming'),
]
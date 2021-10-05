from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('dart_throw.urls')),
    path('', include('swimming.urls')),
    path('admin/', admin.site.urls),
]

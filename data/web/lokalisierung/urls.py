from django.urls import path, include
from . import views


urlpatterns = [
    path("lokalisierung/fp", views.lokalisierungView.fingerprints),
]
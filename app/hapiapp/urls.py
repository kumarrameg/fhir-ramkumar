from django.urls import path
from .views import (
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView,
    EncounterListCreateView,
    EncounterRetrieveUpdateDestroyView,
    ObservationListCreateView,
    ObservationRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('patients/', PatientListCreateView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
    path('encounters/', EncounterListCreateView.as_view(), name='encounter-list'),
    path('encounters/<int:pk>/', EncounterRetrieveUpdateDestroyView.as_view(), name='encounter-detail'),
    path('observations/', ObservationListCreateView.as_view(), name='observation-list'),
    path('observations/<int:pk>/', ObservationRetrieveUpdateDestroyView.as_view(), name='observation-detail'),
]

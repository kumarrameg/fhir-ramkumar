from rest_framework import generics
from .models import Patient, Encounter, Observation
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientSerializer, EncounterSerializer, ObservationSerializer


class _BasePermissionClass:
    """
    Private base class for views with common permission and authentication classes.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class PatientListCreateView(_BasePermissionClass, generics.ListCreateAPIView):
    """
    View for listing and creating patients.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroyView(_BasePermissionClass, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a patient.
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class EncounterListCreateView(_BasePermissionClass, generics.ListCreateAPIView):
    """
    View for listing and creating encounters.
    """
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer

class EncounterRetrieveUpdateDestroyView(_BasePermissionClass, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting an encounter.
    """
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer

class ObservationListCreateView(_BasePermissionClass, generics.ListCreateAPIView):
    """
    View for listing and creating observations.
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

class ObservationRetrieveUpdateDestroyView(_BasePermissionClass, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting an observation.
    """
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

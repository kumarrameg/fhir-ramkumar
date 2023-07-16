from rest_framework import serializers
from .models import Patient, Encounter, Observation

class ObservationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Observation model.
    """
    class Meta:
        model = Observation
        fields = '__all__'

class EncounterSerializer(serializers.ModelSerializer):
    """
    Serializer for the Encounter model.
    """
    observations = ObservationSerializer(many=True, read_only=True)

    class Meta:
        model = Encounter
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Patient model.
    """
    encounters = EncounterSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'

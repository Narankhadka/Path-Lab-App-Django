from rest_framework import serializers
from .models import Patient, Test, LabReport

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["patient_id", "patient_name", "age", "gender"]
        read_only_fields = ["patient_id", "created_at"]

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["id", "test_name", "description", "price", "is_active"]
        read_only_fields = ["id", "created_at"]

class LabReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReport
        fields = ["id", "patient", "test", "status", "result_value", "created_at", "result_date"]
        read_only_fields = ["id", "created_at", "result_date"]


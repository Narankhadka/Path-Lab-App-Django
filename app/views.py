from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Patient,Test,LabReport
from .serializers import PatientSerializer , TestSerializer,LabReportSerializer
# Create your views here.


class PatientViewSet(ModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer



class TestViewSet(ModelViewSet):
    queryset=Test.objects.all()
    serializer_class=TestSerializer


class LabReportViewSet(ModelViewSet):
    queryset = LabReport.objects.all()
    serializer_class = LabReportSerializer


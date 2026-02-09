from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, TestViewSet, LabReportViewSet

router=DefaultRouter()
router.register(r'patients',PatientViewSet,basename='patients')
router.register(r'tests',TestViewSet,basename='tests')
router.register(r'reports',LabReportViewSet,basename='reports')

urlpatterns = router.urls




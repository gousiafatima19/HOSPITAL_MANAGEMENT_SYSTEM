from django.urls import path
from .views import PatientListView, patient_edit, patient_create, patient_delete, PatientListCreateAPI

urlpatterns = [
    path('', PatientListView.as_view()),
    path('<int:pk>/edit', patient_edit),
    path('<int:pk>/delete', patient_delete),
    path('create/', patient_create),
    path('api', PatientListCreateAPI.as_view())
]

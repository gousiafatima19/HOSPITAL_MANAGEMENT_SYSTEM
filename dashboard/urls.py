from django.urls import path
from .views import dashboard_home , dashboard_hms_ai


urlpatterns = [
    path('', dashboard_home),
    path('ai/',dashboard_hms_ai, name='ai'),
]
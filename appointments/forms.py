from django import forms
from .models import Appointment
from patients.models import Patient

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    doctor = forms.IntegerField()
    time = forms.CharField()
    status = forms.CharField()
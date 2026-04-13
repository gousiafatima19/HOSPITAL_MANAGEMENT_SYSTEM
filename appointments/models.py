from django.db import models
class Appointment(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    appointment_time = models.DateTimeField()
    appointment_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment with {self.patient.name} at {self.appointment_time}"

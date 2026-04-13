from django.shortcuts import get_object_or_404, redirect, render
from .models import Patient
from django.utils import decorators
from django import views
# Create your views here.

# def patient_list(request):
#       patients = Patient.objects.all()
#       return render(request, 'list.html',  {'patients': patients})

class PatientListView(views.View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'list.html',  {'patients': patients})
    def post(self, request):
        pass
def patient_edit(request, pk):
          patient = get_object_or_404(Patient, pk=pk)
          if request.method == 'POST':
              patient.name = request.POST.get('name')
              patient.phone = request.POST.get('phone')
              patient.save()
          return render(request, 'patient_edit.html', {'patient': patient})


def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('/patients')

def patient_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        Patient.objects.create(
            name=name,
            phone=phone,
            email=email
        )
        return redirect('/patients')
    return render(request, "patient_create.html")


from rest_framework.generics import ListCreateAPIView
from .serializers import PatientSerializer

class PatientListCreateAPI(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
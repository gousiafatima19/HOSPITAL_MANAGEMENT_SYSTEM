from django.shortcuts import get_object_or_404, render, redirect
from .models import Doctor


# Create your views here.

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doc_list.html', {'doctors': doctors})


def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.save()
        return redirect('/doctors')
    return render(request, 'doc_edit.html', {'doctor': doctor})


def doctor_create(request):
     if request.method == 'POST':
         Doctor.objects.create(
             name = request.POST.get('name'),
             specialization = request.POST.get('specialization')
         )
         return redirect('/doctors')
     return render(request, 'doc_create.html')


def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect('/doctors')
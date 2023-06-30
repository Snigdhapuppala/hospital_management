from django.shortcuts import render, redirect
from .models import Doctor
# Create your views here.
from .forms import DoctorForm
def showAllDoctors(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request, 'showDoctors.html', context)
def doctorDetails(request, pk):
    eachdoctor = Doctor.objects.get(id=pk)
    context = {
        'eachdoctor': eachdoctor
    }
    return render(request, 'doctorDetails.html', context)
def addDoctor(request):
    form = DoctorForm()

    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showDoctors')

    context = {
        'form': form
    }
    return render(request, 'addDoctor.html', context)
def updateDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)

    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('showDoctors')
    context = {
        'form': form
    }
    return render(request, 'updateDoctors.html', context)
def deleteDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()

    return redirect('showDoctors')

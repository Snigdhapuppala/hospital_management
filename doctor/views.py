from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor
# Create your views here.
from .forms import DoctorForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#@login_required(login_url='accounts/login')
def showAllDoctors(request):
    doctors = Doctor.objects.filter(is_available=True).order_by('hospital_name')
    #number_of_doctors = Doctor.objects.all().count()
    #print('Number of Doctors:', number_of_doctors)
    page_num = request.GET.get('page') #creating total pages
    paginator = Paginator(doctors, 3) #setting total no of products in a page
    try:
        doctors = paginator.page(page_num) #21 pages 7 pages created
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)

    context = {
        'doctors': doctors,
        'number_of_doctors': doctors,
    }
    return render(request, 'showDoctors.html', context)
#@login_required(login_url='accounts/login')
def doctorDetails(request, pk):
    eachdoctor = Doctor.objects.get(id=pk)
    context = {
        'eachdoctor': eachdoctor
    }
    return render(request, 'doctorDetails.html', context)
@login_required(login_url='showDoctors')
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
@login_required(login_url='showDoctors')
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
@login_required(login_url='showDoctors')
def deleteDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()

    return redirect('showDoctors')

# creating a function for searching the data from the databse using the keyword
@login_required(login_url='showDoctors')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # value
        if query:
            doctor = Doctor.objects.filter(hospital_name__contains=query)
            return render(request, 'searchbar.html', {"doctor": doctor})
        else:
            print("No Doctors found")
            return render(request, 'searchbar.html', {})



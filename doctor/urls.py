from django.urls import path
from .views import showAllDoctors
from doctor import views


urlpatterns = [
    path('', views.showAllDoctors, name='showDoctors'),
    path('doctor/<int:pk>', views.doctorDetails, name='doctorDetails'),
    path('addDoctor/', views.addDoctor, name='addDoctor'),
    path('updateDoctor/<int:pk>', views.updateDoctor, name='updateDoctor'),
    path('deleteDoctor/<int:pk>', views.deleteDoctor, name='deleteDoctor'),
]

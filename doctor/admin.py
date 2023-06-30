from django.contrib import admin
from .models import Doctor, Category
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hospital_name', 'category', 'is_available')
    list_filter = ('is_available',)
    list_editable = ('is_available',)
    search_fields = ('name', 'hospital_name')
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Category)

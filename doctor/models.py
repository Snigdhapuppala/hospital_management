from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


# Create your models here.
class Doctor(models.Model):
    image = models.ImageField(blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    hospital_name = models.CharField(max_length=200, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

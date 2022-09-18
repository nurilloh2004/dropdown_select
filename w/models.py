from unicodedata import name
from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=125)

class Module(models.Model):
    name = models.CharField(max_length=125)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

class Room(models.Model):
    name = models.CharField(max_length=125)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='modules')
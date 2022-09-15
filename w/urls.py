from django.urls import path
from .views import *


urlpatterns = [
    path('', courses, name='courses'),
    path('modules/', modules, name='modules'),
]
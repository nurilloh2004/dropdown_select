from ast import Mod
from django.core.management.base import BaseCommand
from w.models import *

class Command(BaseCommand):
    help = 'Load Course and Modules'

    def handle(self, *args, **kwargs):
        Module.objects.all().delete()
        course_names = [
            'Computer Science', 'Biologies', 'Mathematics',
        ]

        if not Course.objects.count():
            for course_name in course_names:
                Course.objects.create(name=course_name)

        cs = Course.objects.get(name='Computer Science')

        compsci_modules = [
            'AI',
            'AI',
            'AI',
            'AI',
            'AI',
        ]

        for module in compsci_modules:
            Module.objects.create(name=module, course=cs)
    
    def handle1(self, *args, **kwargs):
        Room.objects.all()
        
        # if not Module.objects.count():
        #     for module_name in module_names:
        #         Course.objects.create(name=module_name)
        md = Module.objects.get(name='AI')

        md_rooms = [
            'First',
            'Second',
            'Third',
            'Fourth',
        ]
        for mdr in md_rooms:
            Room.objects.create(name=mdr, course=md)
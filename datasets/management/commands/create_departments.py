from django.core.management.base import BaseCommand

from datasets.models import Department


class Command(BaseCommand):
    help = 'Create default Departments'

    def handle(self, *args, **options):
        departments_list = ['Geographic Information Infrastructure Division',
                            'Topographic Survey Division',
                            'Geodetic Survey Division',
                            'Cadastral Survey Division'
                            ]
        departments_objects = []
        for department in departments_list:
            department_obj = Department(name=department)
            departments_objects.append(department_obj)
        Department.objects.bulk_create(departments_objects)
        self.stdout.write('Successfully created departments.')

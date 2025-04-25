from django.core.management.base import BaseCommand
from everest_app.models import SeminarSphere


class Command(BaseCommand):
    help = 'Add default seminar formats'

    def handle(self, *args, **kwargs):
        SeminarSphere.objects.bulk_create([
            SeminarSphere(sphere='zakupki'),
            SeminarSphere(sphere='nalogi')
        ])

        print('All default cats updated. Have a nice day!')

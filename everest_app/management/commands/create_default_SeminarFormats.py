from django.core.management.base import BaseCommand
from everest_app.models import SeminarFormat


class Command(BaseCommand):
    help = 'Add default seminar formats'

    def handle(self, *args, **kwargs):
        SeminarFormat.objects.bulk_create([
            SeminarFormat(format='Онлайн'),
            SeminarFormat(format='Очно'),
            SeminarFormat(format='Очно и онлайн')
        ])

        print('All default cats updated. Have a nice day!')

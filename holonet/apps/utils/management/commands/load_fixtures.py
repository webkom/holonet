from django.conf import settings
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = 'Loads initial data from fixtures.'

    def handle(self, *args, **options):
        self.stdout.write('Loading regular fixtures:')

        if settings.DEVELOPMENT:
            self.stdout.write('Loading development fixtures:')
            call_command('loaddata', 'holonet/apps/authorization/fixtures/development_users.yaml')

        self.stdout.write('Done!')

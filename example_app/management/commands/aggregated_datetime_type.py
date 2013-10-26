from django.core.management import BaseCommand
from example_app.models import User
from django.conf import settings

class Command(BaseCommand):
  def handle(self, *opts, **args):
    database_type = settings.DATABASES['default']['ENGINE'].split('.')[-1]
    expiry_dt_type = type(User.objects.all()[0].expiry_dt)
    self.stdout.write('database engine: %s\n' % database_type)
    self.stdout.write('aggregated datatime type: %s\n' % expiry_dt_type)

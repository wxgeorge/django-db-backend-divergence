from django.core.management import BaseCommand
from example_app.models import User

class Command(BaseCommand):
  def handle(self, *opts, **args):
    self.stdout.write('%s\n' % type(User.objects.all()[0].expiry_dt))

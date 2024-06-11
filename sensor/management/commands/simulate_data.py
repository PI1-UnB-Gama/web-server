from django.core.management.base import BaseCommand
from sensor.models import SensorData
from sensor.views import simulate_path
from django.utils import timezone

class Command(BaseCommand):
    help = 'Simulate sensor data'

    def handle(self, *args, **kwargs):
        path = simulate_path()
        for x, y in path:
            SensorData.objects.create(x=x, y=y, timestamp=timezone.now())
        self.stdout.write(self.style.SUCCESS('Successfully simulated sensor data'))

from django.core.management.base import BaseCommand
from sensor.models import SensorData
from sensor.views import simulate_path
from django.utils import timezone
import csv

class Command(BaseCommand):
    help = 'Simulate sensor data'

    def handle(self, *args, **kwargs):
        f = open("mock.csv")
        data = csv.reader(f)

        for row in data:
            timestamp, x, y, power_current = row
            SensorData.objects.create(timestamp=timestamp, x=x, y=y, power_current=power_current)

        f.close()
        print("Dados inseridos com sucesso.")


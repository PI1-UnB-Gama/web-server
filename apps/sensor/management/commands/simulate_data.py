import csv

from django.core.management.base import BaseCommand
from sensor.models import SensorData


class Command(BaseCommand):
    help = "Simulate sensor data"

    def handle(self, *args, **kwargs):
        f = open("mock.csv")
        data = csv.reader(f)

        for row in data:
            timestamp, rotations, pulses, x, y, volts, diameter = row
            SensorData.objects.create(timestamp=timestamp, x=x, y=y)

        f.close()
        print("Dados inseridos com sucesso.")

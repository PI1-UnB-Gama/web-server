from django.db.models import Model, DateTimeField, FloatField
from django.utils import timezone

class SensorData(Model):
    timestamp = DateTimeField(default=timezone.now)
    x = FloatField()
    y = FloatField()
    power_current = FloatField()

    def __str__(self) -> str:
        return f"{self.timestamp} - ({self.x}, {self.y})"

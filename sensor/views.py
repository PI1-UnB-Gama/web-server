import json
import math
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from .models import SensorData


def receive_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        values = data.get('values')

        if values is None:
            return JsonResponse({'status': 'error', 'message': 'Invalid data'})

        for value in values:
            if value is not None:
                x = value["x"]
                y = value["y"]
                timestamp = value["timestamp"]
                SensorData.objects.create(x=x, y=y, timestamp=timestamp)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def simulate_path():
    path = []
    x, y = 0, 0
    for _ in range(100):
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, 5)
        x += distance * math.cos(angle)
        y += distance * math.sin(angle)
        path.append((x, y))
    return path


def plot_data(request):
    data = SensorData.objects.all().order_by('timestamp')
    x_coords = [d.x for d in data]
    y_coords = [d.y for d in data]
    return render(request, 'sensor/plot.html', {
        'x_coords': json.dumps(x_coords),
        'y_coords': json.dumps(y_coords),
    })
import json
import math
import random

from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.http.request import HttpRequest
from django.http.response import JsonResponse

from .models import SensorData


def receive_data(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

    data = json.loads(request.body)
    values = data.get('values')

    if values is None:
        return JsonResponse({'status': 'error', 'message': 'Invalid data'})

    for value in values:
        if value is None:
            continue

        timestamp = value["timestamp"]
        x = value["x"]
        y = value["y"]
        power_current = value["power_current"]
        SensorData.objects.create(timestamp=timestamp, x=x, y=y, power_current=power_current)

    return JsonResponse({'status': 'success'})

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
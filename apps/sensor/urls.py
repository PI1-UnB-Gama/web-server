from django.urls import path

from .views import plot_data, receive_data

urlpatterns = [
    path("receive-data/", receive_data, name="receive_data"),
    path("plot-data/", plot_data, name="plot_data"),
]

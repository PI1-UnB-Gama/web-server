from django.urls import path
from .views import receive_data, plot_data

urlpatterns = [
    path('receive-data/', receive_data, name='receive_data'),
    path('plot-data/', plot_data, name='plot_data'),
]

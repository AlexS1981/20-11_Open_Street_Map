from django.shortcuts import render

# Create your views here.


def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiYWxleHZzIiwiYSI6ImNraTk0b3BtcjBjOWMycmxiZTVoejhsaTcifQ._GauRo7uCwtAgWAHnwd8kQ'

    data = {'mapbox_access_token': mapbox_access_token,
            'latitude': 48.4676804,
            'longitude': 35.0406599,
            'box_lat_a': 34.9690532,
            'box_lon_a': 48.4444046,
            'box_lat_b': 35.1123905,
            'box_lon_b': 48.4914684,
            'zoom': 9
            }

    return render(request, 'default.html', context=data)

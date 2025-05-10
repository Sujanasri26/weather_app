import requests
from django.shortcuts import render
from .forms import CityForm
from django.conf import settings
API_KEY = settings.OPENWEATHER_API_KEY


def landing_page(request):
    return render(request, 'landing_page.html')
def weather_view(request):
    weather_data = {}
    error_msg = None

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            API_KEY = '87306ac8f46cc894d681eef943419439'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error_msg = data.get('message', 'City not found')
    else:
        form = CityForm()

    return render(request, 'weather.html', {'form': form, 'weather': weather_data, 'error': error_msg})

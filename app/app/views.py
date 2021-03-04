from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from .models import Records
import requests
import json
import datetime

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def get_temperature(request):
    city = request.GET["location"]

    db_response = db_call(city)
    
    if db_response != None:
        return JsonResponse(db_response, safe=False)
    else:
        return JsonResponse( api_call(city) )

def db_call(city):
    response = Records.objects.filter(city_name=city).values()
    
    if response:
        return list(response)[0]
    else:
        return None

def api_call(city):

    try:
        location = requests.get('https://eu1.locationiq.com/v1/search.php?key=a1779b7817b3b2&q='+city+'&format=json')
        json_location = location.json()
        lat = json_location[0]['lat']
        lon = json_location[0]['lon']

        weather = requests.get('https://api.darksky.net/forecast/f3146e0fc78b4930d41a60703c08e2ae/'+lat+','+lon+'?units=si')
        
        weather_obj = weather.json()

        cur_time = weather_obj['currently']['time']
        cur_temp = weather_obj['currently']['temperature']

        temp_array = []
        temp_weekly_array = []

        for hour in weather_obj['hourly']['data']:
            if (hour['time'] < weather_obj['daily']['data'][1]['time']) and (hour['time'] > cur_time):
                temp_array.append(hour['temperature'])
        
        for day in weather_obj['daily']['data']:
            temp_weekly_array.append(day['temperatureHigh'])
            temp_weekly_array.append(day['temperatureLow'])

        temp_array.sort()
        today_min_temp = temp_array[0]
        today_max_temp = temp_array[-1]

        temp_weekly_array.sort()
        week_min_temp = temp_weekly_array[0]
        week_max_temp = temp_weekly_array[-1]

        response_obj = {
            "city_name" : city,
            "current_temperature" : cur_temp,
            "today_min_temperature" : today_min_temp,
            "today_max_temperature" : today_max_temp,
            "this_week_min_temperature" : week_min_temp,
            "this_week_max_temperature" : week_max_temp
        }

        Records.objects.create(city_name=city, current_temperature=cur_temp, 
            today_min_temperature=today_min_temp, today_max_temperature=today_max_temp,
            this_week_min_temperature=week_min_temp, this_week_max_temperature=week_max_temp)

        return response_obj         
        
    except:
        HttpResponse("Something went wrong")
    
    
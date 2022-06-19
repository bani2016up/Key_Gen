import requests

API_KEY = '61051d147f304411804184153221506'
location = 'Moscow'
FIRST_URL = 'http://api.weatherapi.com/v1/current.json?key=' + API_KEY + '&q=' + location + '&aqi=yes'

bool = str(input('Get a random Number? [y/n]: '))

def get_random_num(bool, URL):
    if bool == 'y':
        req = requests.get(URL)
        if req.status_code == 200:
            res = req.json()
            temp_c = float(res['current']['temp_c'])
            temp_f = float(res['current']['temp_f'])
            wind_kph = float(res['current']['wind_kph'])
            wind_degree = float(res['current']['wind_degree'])
            uv = float(res['current']['uv'])
            pm10 = float(res['current']['air_quality']['pm10'])
            
            stage_one = round(temp_c / temp_f * wind_degree / wind_kph * uv / pm10, 2)
            stage_two = stage_one ** 2 % 6
            print(stage_two)

            
        
get_random_num(bool, FIRST_URL)
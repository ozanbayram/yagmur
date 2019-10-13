import json
import requests
from requests import get

import datetime
from datetime import datetime as dt

class Configs:
    def confRead(self):
        path = 'conf.json'
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def utc_to_dt(self, _utc: int):
        date = dt.fromtimestamp(
            _utc, tz=datetime.timezone.utc)

        date = date.strftime('%I.%M %d.%m.%Y')
        return date
    
    def fah_to_cel(self, _fah: int):
        cal = (_fah - 32) * (5 / 9)
        return round(cal, 1)

    def mile_to_kilom(self, _mil: int):
        cal = _mil * (8 / 5)
        return round(cal)
        
class Weather(Configs):
    def __init__(self):
        conf = self.confRead()
        
        self.LAT = conf['lat']
        self.LON = conf['lon']
        self.LANG = conf['api']['lang']
        self.EXCLUDE = conf['api']['exclude']
        self.KEY = conf['api']['key']

        main = 'https://api.darksky.net/forecast/'
        self.url = main+'{}/{},{}?lang={}&exclude={}'.format(
            self.KEY, self.LAT, self.LON, self.LANG, self.EXCLUDE)

    def get_data(self):
        try:
            request = get(self.url)
        except:
            raise ConnectionError('Ağ sorunu!')
            
        data = request.json()
        currently = data['currently']

        time = currently['time']
        summary = currently['summary']
        icon = currently['icon']
        
        temperature = currently['temperature']
        humidity = currently['humidity']
        uvindex = currently['uvIndex']
        visibility = currently['visibility']
        dewPoint = currently['dewPoint']
        pressure = currently['pressure']
        
        return (
            [self.utc_to_dt(time), summary, icon],
            [self.fah_to_cel(temperature), humidity,
             uvindex, self.mile_to_kilom(visibility),
             self.fah_to_cel(dewPoint), pressure]
            )

from datetime import datetime

class Weather:
    def __init__(self, data):
        self.coord = data.get('coord', {})
        self.weather = data.get('weather', [{}])[0]
        self.base = data.get('base', '')
        self.main = data.get('main', {})
        self.visibility = data.get('visibility', 0)
        self.wind = data.get('wind', {})
        self.clouds = data.get('clouds', {})
        self.dt = data.get('dt', 0)
        self.sys = data.get('sys', {})
        self.timezone = data.get('timezone', 0)
        self.id = data.get('id', 0)
        self.name = data.get('name', '')
        self.cod = data.get('cod', 0)

    def __str__(self):
        return str({
            'coord': self.coord,
            'weather': self.weather,
            'base': self.base,
            'main': self.main,
            'visibility': self.visibility,
            'wind': self.wind,
            'clouds': self.clouds,
            'dt': self.dt,
            'sys': self.sys,
            'timezone': self.timezone,
            'id': self.id,
            'name': self.name,
            'cod': self.cod
        })
    def curentTime():
        return  datetime.now().strftime("%d/%m/%y, %H:%M:%S")
    
    def timestampToHoursMinutes(timestamp):
        return datetime.fromtimestamp(timestamp).strftime('%H:%M')
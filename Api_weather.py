from pprint import pprint
import requests
url = 'http://api.openweathermap.org/data/2.5/weather?q=hawassa,Ethiopia&units=imperial&appid=a1e726af4a3e233a78112400e90bbd56'
data = requests.get(url).json()
#pprint(data
temperature = data['main']['temp']
cityName = data['name']
print(f'the temperature in {cityName} is {temperature}' )

# import the json library
import json

# open the json file and assign it to a variable
jsonWeatherData=open('IDV60801.94857.json')

# convert the json data into a python dictionary
weatherData=json.load(jsonWeatherData)

# access the python dictionary and print the relevant data
print(weatherData['observations']['data'][0]['air_temp'])

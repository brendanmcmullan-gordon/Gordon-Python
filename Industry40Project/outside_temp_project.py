# import json, urllib3 and mysql.connector
import json
import urllib3
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password1",
    database=""
)

c = db.cursor()

# use urllib3 and go through a proxy to access the internet
# http = urllib3.PoolManager < no proxy
httpproxy = urllib3.ProxyManager('http://192.168.210.6:3128')

# send a get request for the .json file from the BOM
jsondata = httpproxy.request('GET', 'http://www.bom.gov.au/fwo/IDV60801/IDV60801.94857.json')

# decode the file into utf-8, then read it with the json library and convert it to a python object
weatherdata = json.loads(jsondata.data.decode('utf-8'))

# access the air temp key from the converted dictionary
airtemp = str(weatherdata['observations']['data'][0]['air_temp'])

# other
# print("The air temperature at Geelong Racecourse is", weatherdata['observations']['data'][0]['air_temp'], "degrees C")
# print("The relative humidity at Geelong Racecourse is", weatherdata['observations']['data'][0]['rel_hum'], "%")
# print("The wind speed at Geelong Racecourse is", weatherdata['observations']['data'][0]['wind_spd_kmh'], "km/h")

# insert airtemp into a mysql db
sql = ("INSERT INTO weather (OUTSIDETEMP) VALUES (%s)")
val = (airtemp,)
c.execute(sql, val)
db.commit()

c.close()
db.close()

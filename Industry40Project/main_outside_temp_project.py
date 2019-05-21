# import json, urllib3 and mysql.connector
import json
import urllib3
import datetime
import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password1",
    database="Industry40DB"
)

c = db.cursor()

# attempt to create a table and throw an error if it already exists
try:
    c.execute("CREATE TABLE weatherData ("
              "ID INT AUTO_INCREMENT PRIMARY KEY,"
              "TIME_STAMP TIMESTAMP,"
              "OUTSIDETEMP VARCHAR(4),"
              "LOCAL_DATE_TIME DATETIME)")
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)

# use urllib3 and go through a proxy to access the internet
# http = urllib3.PoolManager < no proxy
httpproxy = urllib3.ProxyManager('http://192.168.210.6:3128')

# send a get request for the .json file from the BOM
jsondata = httpproxy.request('GET', 'http://www.bom.gov.au/fwo/IDV60801/IDV60801.94857.json')

# decode the file into utf-8, then read it with the json library and convert it to a python object
weatherdata = json.loads(jsondata.data.decode('utf-8'))

# access the air temp and local date time keys from the converted dictionary
airtemp = str(weatherdata['observations']['data'][0]['air_temp'])
localdatetime = str(weatherdata['observations']['data'][0]['local_date_time'])

# get today's date
today = str(datetime.date.today())

# strip the day from today's date
yrmonth = '{:.8}'.format(today)

# split the BOM datetime into day and time
splitstr = localdatetime.split('/')

# set day to the first in the split list
day = splitstr[0]

# split the time string into hours and minutes
timelist = splitstr[1].split(':')

# set hrs to the first in the time list
hrs = timelist[0]

# if pm is on the end of the minutes, add 12 to 'convert' to 24-hour time
if splitstr[1].endswith('pm') == True:
    hrs = int(hrs)
    hrs += 12
    hrs = str(hrs)

# set min to the second in the time list
min = timelist[1]

# strip am or pm from the end of the minutes
min = min.rstrip('apm')

# create the datetime string for sql
format_date_time = str(yrmonth+day+" "+hrs+":"+min+":00")

# other
# print("The air temperature at Geelong Racecourse is", weatherdata['observations']['data'][0]['air_temp'], "degrees C")
# print("The relative humidity at Geelong Racecourse is", weatherdata['observations']['data'][0]['rel_hum'], "%")
# print("The wind speed at Geelong Racecourse is", weatherdata['observations']['data'][0]['wind_spd_kmh'], "km/h")

# insert airtemp and datetime into a mysql db
sql = ("INSERT INTO weatherData (OUTSIDE_TEMP, LOCAL_DATE_TIME) VALUES (%s, %s)")
val = (airtemp, format_date_time)
c.execute(sql, val)
db.commit()

c.close()
db.close()

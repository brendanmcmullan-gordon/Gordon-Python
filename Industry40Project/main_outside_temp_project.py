# import json, urllib3 and mysql.connector
import json
import urllib3
import datetime
import mysql.connector
from mysql.connector import errorcode

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Password1",
        database="Industry40DB"
    )

    c = db.cursor(buffered=True)
# catch any mysql errors occurring on connecting to the db
except mysql.connector.Error as err:
    print(err.errno, err.msg)
    exit()

# attempt to create a table and throw an error if it already exists
try:
    c.execute("CREATE TABLE weatherData ("
              "ID INT AUTO_INCREMENT PRIMARY KEY,"
              "TIME_STAMP TIMESTAMP,"
              "OUTSIDE_TEMP VARCHAR(4),"
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

# access the air temp and datetime keys from the converted dictionary
airtemp = str(weatherdata['observations']['data'][0]['air_temp'])
ldtstr = str(weatherdata['observations']['data'][0]['local_date_time_full'])

# ldtformat = formatDateTime(localdatetime)
ldtformat = ldtstr[0:4] + "-" + ldtstr[4:6] + "-" + ldtstr[6:8] + " " + ldtstr[8:10] + ":" + ldtstr[10:12] + ":" + ldtstr[12:14]

try:
    # fetch the datetime from the last inserted row
    c.execute("SELECT LOCAL_DATE_TIME FROM weatherData ORDER BY ID DESC LIMIT 1")
    olddatetime = c.fetchone()[0]
    olddatetime = str(olddatetime)


    # insert airtemp and datetime into a mysql db if the datetime has been updated
    if not ldtformat == olddatetime:
        sql = ("INSERT INTO weatherData (OUTSIDE_TEMP, LOCAL_DATE_TIME) VALUES (%s, %s)")
        val = (airtemp, ldtformat)
        c.execute(sql, val)
        db.commit()
    elif ldtformat == olddatetime:
        print("Temperature not updated, skipping table insert.")

# if there are no entries in the table, insert an entry without checking for the last datetime
except TypeError:
    sql = ("INSERT INTO weatherData (OUTSIDE_TEMP, LOCAL_DATE_TIME) VALUES (%s, %s)")
    val = (airtemp, ldtformat)
    c.execute(sql, val)
    db.commit()
    print("Inserting first value")


c.close()
db.close()

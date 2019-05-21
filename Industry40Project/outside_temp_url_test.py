# import json and urllib3
import json
import urllib3

# use urllib3 and go through a proxy to access the internet
# http = urllib3.PoolManager
httpproxy = urllib3.ProxyManager('http://192.168.210.6:3128')

# send a get request for the .json file from the BOM
jsondata = httpproxy.request('GET', 'http://www.bom.gov.au/fwo/IDV60801/IDV60801.94857.json')

# decode the file into utf-8, then read it with the json library and convert it to a python object
weatherdata = json.loads(jsondata.data.decode('utf-8'))

# access the air temp key from the converted dictionary
print("The air temperature at Geelong Racecourse is", weatherdata['observations']['data'][0]['air_temp'], "degrees C")
print(weatherdata['observations']['data'][0]['local_date_time'])
# other


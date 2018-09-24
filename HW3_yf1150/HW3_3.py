import sys
import urllib.request, json 

#print(sys.argv)

input_key = sys.argv[1]
input_line = sys.argv[2]

URL = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(input_key, input_line)


with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    #print(data)
    bus_data = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    number_of_bus = len(bus_data)
    location = [(i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"], i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]) for i in bus_data  ]
    #print(bus_data[0]["MonitoredVehicleJourney"]["VehicleLocation"])
    
print("Bus Line : {}".format(input_line))
print("Numebr of Active Buses : {}".format(number_of_bus))
for i in range(number_of_bus):
    print("Bus {} is at latitude {} and longitude {}".format(i, location[i][0], location[i][1]))

import sys
import urllib.request, json 

# print(sys.argv)

# check if the number of arguements is correct
if len(sys.argv) != 3:
    print("Invalid inputs. Please run as python3 HW3_3.py <MTA_API_KEY> <BUS_LINE>")
    sys.exit()

input_key = sys.argv[1]
input_line = sys.argv[2]

URL = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(input_key, input_line)

# read data from MTA
with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    bus_list = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    number_of_bus = len(bus_list)
    location = [(i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"], i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]) for i in bus_list]
    
# print bus number and bus locations to terminal
print("Bus Line : {}".format(input_line))
print("Numebr of Active Buses : {}".format(number_of_bus))
for i in range(number_of_bus):
    print("Bus {} is at latitude {} and longitude {}".format(i, location[i][0], location[i][1]))

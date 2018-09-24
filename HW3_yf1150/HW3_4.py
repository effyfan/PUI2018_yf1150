import sys
import urllib.request, json 
import csv

#print(sys.argv)

input_key = sys.argv[1]
input_line = sys.argv[2]
input_filename = sys.argv[3]

URL = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(input_key, input_line)


with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    #print(data)
    bus_list = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
    number_of_bus = len(bus_list)
    record = []
    for i in bus_list:
        item = {}
        item["stop_name"] = "N/A"
        item["stop_status"] = "N/A"
        if len(i["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]) > 0:
            item["stop_name"] = i["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
            item["stop_status"] = i["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
        item["lat"] = i["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        item["long"] = i["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        record.append(item)

with open(input_filename, 'w') as csvfile:
    fieldnames = ['Latitude','Longitude','Stop Name','Stop Status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    # for item in range(number_of_bus):
        # spamwriter.writerow([location[i][0], location[i][1], stopname, stop_status])
    for i in record:
        writer.writerow({'Latitude': i["lat"], 'Longitude': i["long"], 'Stop Name': i["stop_name"], 'Stop Status': i["stop_status"]})
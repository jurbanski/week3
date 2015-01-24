#!/usr/local/bin/python3
""" Week 3 Homework, Divvy bike problem """
# 2015-01-23
# Joseph Urbanski
# MPCS 50101

# Imports:
import math
import json
from urllib.request import urlopen

def main():
    """ Main function """
    # URL for Divvy's JSON feed.
    webservice_url = 'http://www.divvybikes.com/stations/json'
    # Open and read the JSON info from Divvy's feed.
    data = urlopen(webservice_url).read().decode('utf8')
    result = json.loads(data)
    # Strip the top level JSON info so we get only the stations and their info.
    stations = result['stationBeanList']

    # Initialize some variables we'll need outside of the for loop below.
    closest_station_name = ''
    closest_station_num_bikes = 0
    shortest_dist = 180            # The farthest possible distance, in degrees

    # Latitude and longitude for the Young building
    young_lat = 41.793414
    young_long = -87.600915

    # Loop over all stations in the JSON feed ...
    for i in stations:
        # ... calculating the distance to that station ...
        distance = math.sqrt(pow((young_lat - i['latitude']), 2) + \
                             pow((young_long - i['longitude']), 2))
        # ... and storing the distance, station name, and number of available
        # bikes if it is closer than the previously found closest station.
        if distance < shortest_dist:
            closest_station_name = i['stationName']
            closest_station_num_bikes = i['availableBikes']
            shortest_dist = distance

    # Output the name of the closest station and the number of available bikes.
    print("The nearest station is:", closest_station_name)
    print("There are", closest_station_num_bikes, "bikes currently available.")

main()

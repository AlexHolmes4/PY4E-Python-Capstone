import sqlite3
import time
import zlib

conn = sqlite3.connect('fstructureddata.sqlite')
cur = conn.cursor()

cur.execute('SELECT id, population_count FROM demography ORDER BY id')
demographies = dict()
for demography_row in cur :
    demographies[demography_row[0]] = demography_row[1]
#print(demographies
cur.execute('SELECT id, city FROM location ORDER BY id')
locations = dict()
for location_row in cur :
    locations[location_row[0]] = location_row[1]

# cur.execute('SELECT id, guid,sender_id,subject_id,headers,body FROM Messages')
cur.execute('''
SELECT flight.id, passengers, seats, stops, distance, origin.city, destination.city, demography.date
FROM `flight`
INNER JOIN `location` as origin ON flight.location_id_orig=origin.id
INNER JOIN `location` as destination ON flight.location_id_dest=destination.id
INNER JOIN `demography` ON flight.demography_id=demography.id
ORDER BY flight.id''')
flights = dict()
for flight_row in cur :
    flights[flight_row[0]] = (flight_row[1],flight_row[2],flight_row[3],flight_row[4],flight_row[5],flight_row[6],flight_row[7])

passengerscount = dict()
emptyseatscount = dict()
flightsfromcount = dict()
flightstocount = dict()
total_seats_empty = 0

                                                  #flight id[0] is 1 next iteration 2, etc. Wheras flight id[1] is the tuple (0,0,1,156 etc.)
#create histograms and data points                #by specifying a second iteration variable we access the second value i.e. the tuple
for (flight_id, flight) in list(flights.items()): #list snippit [(1, (0, 0, 1, 156, 1, 2, 1)), (2, (124, 124, 1, 858, 3, 4, 2))
    passengers, seats, stops, distance, origin_city, destination_city = flight[0], flight[1], flight[2], flight[3], flight[4], flight[5]

    passengerscount[passengers] = passengerscount.get(passengers,0) + 1

    seatsempty = seats - passengers
    emptyseatscount[seatsempty] = emptyseatscount.get(seatsempty, 0) + 1
    total_seats_empty = total_seats_empty + seatsempty

    flightsfromcount[origin_city] = flightsfromcount.get(origin_city, 0) + 1

    flightstocount[destination_city] = flightstocount.get(destination_city, 0) + 1

print("Loaded flights=",len(flights),"locations=",len(locations),"demographies=",len(demographies),"empty-seats=",total_seats_empty)

print('')
print('Top Fly to Locations')
x = sorted(flightstocount.items(), reverse=True)
for key, value in x:
    print(value,"flights to", key)

print('')
print('Top Fly From Locations')
x = sorted(flightsfromcount.items())
for key, value in x:
    print(value,"flights from", key)

import sqlite3

conn = sqlite3.connect('fstructureddata.sqlite')
cur = conn.cursor()

# connection to raw data database established for data extraction
conn_raw = sqlite3.connect('file:rawfdata.sqlite?mode=ro', uri=True)
cur_raw = conn_raw.cursor()

# The flight data model program will start a fresh each time.
cur.execute('''DROP TABLE IF EXISTS location ''')
cur.execute('''DROP TABLE IF EXISTS demography ''')
cur.execute('''DROP TABLE IF EXISTS flight ''')

cur.execute('''CREATE TABLE IF NOT EXISTS location
        (id INTEGER PRIMARY KEY UNIQUE, airport_name TEXT UNIQUE,
         city TEXT UNIQUE)''')
cur.execute('''CREATE TABLE IF NOT EXISTS demography
        (id INTEGER PRIMARY KEY UNIQUE, population_count INTEGER,
        date INTEGER, location_id INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS flight
        (id INTEGER PRIMARY KEY UNIQUE, passengers INTEGER, seats INTEGER,
        stops INTEGER, distance INTEGER, location_id_orig INTEGER,
        location_id_dest INTEGER, demography_id INTEGER)''')



# the location table is the first to recieve data, as it uses no foreign keys (end of branch)
# We handle this with a while loop and two INSERT OR IRGNORE's per iteration, one gatherng the origin the other the destination.
count = 1
while True:
    # fetch row of raw flight data
    cur_raw.execute('''SELECT origin, destination, origin_city, destination_city, passengers, seats, stops, distance, fly_date,
    origin_population, destination_population FROM flights_raw WHERE id = ?''', (count, ))
    try:
        row = cur_raw.fetchone()
        print("raw data retrieved for cleaning and modelling:\n",row,'\n')
    except:
        print("location table import complete")
        break
    if row is None:
        print("Modelling complete.")
        break

    # location table
    # insert origin to location table
    cur.execute('''INSERT OR IGNORE INTO location (airport_name, city)
        VALUES (?, ?)''', (row[0], row[2]))
    conn.commit()
    # retrieve the id for the origin location
    cur.execute('SELECT id FROM location WHERE airport_name = ?', (row[0], ))
    origin_id = cur.fetchone()[0]

    # insert destination to location table
    cur.execute('''INSERT OR IGNORE INTO location (airport_name, city)
        VALUES (?, ?)''', (row[1], row[3]))
    conn.commit()
    # retrieve the id for the destination location
    cur.execute('SELECT id FROM location WHERE airport_name = ?', (row[1], ))
    destination_id = cur.fetchone()[0]

    # demography table
    #insert origin to demography table
    cur.execute('''INSERT INTO demography (population_count, date,
    location_id) VALUES (?, ?, ?)''', (row[9], row[8], origin_id))
    conn.commit()
    #insert destination to demography table
    cur.execute('''INSERT INTO demography (population_count, date,
    location_id) VALUES (?, ?, ?)''', (row[10], row[8], destination_id))
    conn.commit()

    #retrieve the id for the demography insert
    #only 1 id for the the two (origin, destination) inserts needed as shared date
    cur.execute('SELECT id FROM demography WHERE id = ?', (count, ))
    demography_id = cur.fetchone()[0]

    # flight Table
    cur.execute('''INSERT INTO flight (passengers, seats, stops, distance,
    location_id_orig, location_id_dest, demography_id)
    VALUES (?, ?, ?, ?, ?, ?, ?)''', (row[4],row[5],row[6],row[7], origin_id,
    destination_id, demography_id))
    conn.commit()

    print("id's retrieved:\n","origin_id:",origin_id, " destination_id:",destination_id, " demography_id:",demography_id)
    count = count + 1

conn.close()
conn_raw.close()

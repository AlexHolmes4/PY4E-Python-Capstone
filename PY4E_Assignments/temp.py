import sqlite3
import re

conn = sqlite3.connect('TMS.db')
cur = conn.cursor()

#gather user choice
while True:
    initial_input = input('''
    Add a "Genre"?\n
    Add an "Artist"?\n
    Add an "Album"?\n
    Add a "Track"?\n
    "Exit" the app?\n\n
    Type what you want to do: ''')

    try: initial_input = initial_input.casefold()
    except: continue

    if len(initial_input) < 1 : break #another program exit method

#create an artist
    #obtain user input of artist name
    elif re.search('artist', initial_input):
        while True:
            artist_input = input("Provide Artist Name: ")
            if len(artist_input) < 1:
                print("please provide a value")
                continue
            else: break
        #check DB for that artist Name
        cur.execute('''SELECT name FROM Artist WHERE name = ?''', (artist_input, ))
        try:
            artist_name = cur.fetchone()[1]
            print("Artist with that name already found in our records")
        #if not in DB Insert
        except:
            cur.execute('''INSERT into Artist (name) VALUES (?)''', (artist_input, ))
        #provided back as output what is stored in the Artist Table
        for tuple in cur.execute('SELECT * FROM Artist'):
            print(str(tuple[0]), tuple[1])

#create a genre
    elif re.search('genre', initial_input):
        while True:
            genre_input = input("Provide a Genre: ")
            if len(genre_input) < 1:
                print("please provide a value")
                continue
            else: break
        #check DB for that genre
        cur.execute('''SELECT name FROM Genre WHERE name = ?''', (genre_input, ))
        try:
            genre_name = cur.fetchone()[1]
            print("That genre is already found in our records")
        #if not in DB Insert
        except:
            cur.execute('''Insert into Genre (name) Values (?)''', (genre_input, ))
        #provided back as output what is stored in the Genre Table
        for tuple in cur.execute('SELECT * FROM Genre'):
            print(str(tuple[0]), tuple[1])

#create a track, track must have album and genre in DB, if not navigate user back to create the dependant variables first
    elif re.search('track', initial_input):
        while True:
            track_input = input("Provide a Track Title: ")
            if len(track_input) < 1:
                print("please provide a value")
                continue

            #DB search not needed. Many tracks of same name exist.
            #obtain rating for track
            while True:
                rating_input = input('How many stars out of 5 would you give this track?\nType "skip" to skip this step')
                if len(rating_input) < 1:
                    print('please provide a value, or type "skip"')
                    continue
                elif re.search('skip',rating_input):
                    rating_input = None #might break here try a skip and see
                    break #exits the ratings code flow, to continue the track flow
                else:
                    #see if rating provided is valid number between 1 and 5
                    try:
                        rating_input = int(rating_input)
                        if rating_input > 5 or rating_input < 1:
                            print('please provide a number from 1 - 5 for the rating')
                            continue #restart ratings loop
                        else: break #exit ratings flow as rating is valid for entry
                    except:
                        print("please provide a number from 1 - 5")
                        continue

            #obtain genre for track
            while True:
                genre_input = input("What is the genre of this track?: ")
                if len(genre_input) < 1:
                    print("please provide a value")
                    continue
                else:
                    #check DB for that genre
                    cur.execute('''SELECT * FROM Genre WHERE name = ?''', (genre_input,))
                    try:
                        genre_id = cur.fetchone()[0]
                        break
                    except:
                        print("That genre was not found in our records, please add the genre first.") #this is where I WOULD use SOA Functional modularity, but all things in good time.
                        break
            break #exit code flow block for genre input

            while True:
                album_input = input("What album is this track from?: ")
                if len(album_input) < 1:
                    print("please provide a value")
                    continue
                else:
                    #check DB for the album
                    cur.execute('''SELECT * FROM Album WHERE title = ?''', (album_input,))
                    try:
                        album_id = cur.fetchone()[0]
                    except:
                        print("That album was not found in our records, please add the album first.") #this is where I WOULD use SOA Functional modularity, but all things in good time.
                    break
            break #exit code flow block for album input

        #take all the inputs for track and insert a new tuple into the track table
        cur.execute('''Insert into Track (title, rating, len, count, album_id, genre_id) Values (?, ?, 0, 0, ?, ?)''', (track_input,rating_input,album_id,genre_id, ))
        #provide back output for what is in the Track table
        for tuple in cur.execute('SELECT * FROM Track'):
            print(str('id',tuple[0], 'title',tuple[1], 'album id',tuple[2], 'genre id',tuple[3], 'track length',tuple[4], 'track rating',tuple[5], 'times track played',tuple[6]))

#create an album
    elif re.search('album', initial_input):
        while True:
            album_input = input("Provide an Album Title: ")
            if len(album_input) < 1:
                print("please provide a value")
                continue
            else:
                #check DB for that genre
                cur.execute('''SELECT title FROM Album WHERE title = ?''', (album_input, ))
                try:
                    album_name = cur.fetchone()[1]
                    print("That album is already found in our records")
                    break
                #if not in DB continue with code flow block and gather artist for album
                except:
                    #gather user input for artist
                    while True:
                        artist_input = input("Who is the main artist of the album?: ")
                        if len(artist_input) < 1:
                            print("please provide a value")
                            continue
                        else:
                            #search DB for that artist
                            cur.execute('''SELECT * FROM Artist WHERE name = ?''', (artist_input,))
                            try: #artist found in DB
                                artist_id = cur.fetchone()[0]
                            except: #artist not found
                                print("That artist was not found in our records, please add the artist first.") #this is where I WOULD use SOA Functional modularity, but all things in good time.
                                break #escape code block flow to skip execution of new album
                            cur.execute('''Insert into Album (title, artist_id) Values (?,?)''', (album_input, artist_id))
                            #provide back output for what is in the Album table
                            for tuple in cur.execute('SELECT * FROM Album'):
                                print(tuple[0], tuple[1], tuple[2])
                            break
                    break #break out of album code block
#exit program
    elif re.search('exit', initial_input) or re.search('close', initial_input):
        break
#show options again
    else: continue

    conn.commit()

cur.close()

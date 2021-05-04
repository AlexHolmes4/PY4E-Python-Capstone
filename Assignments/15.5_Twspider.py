import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json
import sqlite3

#API REST URL
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

#Connect to SQLite DB/Create
conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')

#ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #get a new Twitter name, find one from DB (not already retrieved), or quit
    acct = input('Enter a Twitter Account, Expand existing DB (hit Enter), or type "quit" :')
    if (acct == 'quit'): break
    elif (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 Limit 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print("No untretrieved Twitter accounts found")
            continue
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)

    #connect to API with the REST URL
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    #How many API calls remaining
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    # Debugging
    # print(json.dumps(js, indent=4))

    #Set the name being searched as retireved so not used again
    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))


    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
            countold = countold + 1
        except:
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, '  revisited=', countold)
    conn.commit()

cur.close()

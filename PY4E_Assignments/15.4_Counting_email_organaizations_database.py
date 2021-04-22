import sqlite3

conn = sqlite3.connect('SQLiteDB.sqlite') #checks access to the file
cur = conn.cursor() #like a handle

#if a 'Counts' table exists delete it, if not do nothing.
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)') #creates counts table

#read through a file, update to DB every organization that sent an email, and count the number of emails sent from each organization
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1] #returns the email address
    orgpos = email.find('@')
    org = email[orgpos+1:]

    cur.execute('''SELECT count FROM Counts WHERE org = ? ''', (org,))
    row = cur.fetchone() #return what the select statement found
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,)) #if not in org column, insert org and count = 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

    conn.commit()

#return the results after file parsing to DB (effectively a histogram dictionary is made but in the DB)
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close() #close the cursor instance

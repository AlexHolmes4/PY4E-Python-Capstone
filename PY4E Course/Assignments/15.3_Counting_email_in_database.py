import sqlite3

conn = sqlite3.connect('SQLiteDB.sqllite') #checks access to the file
cur = conn.cursor() #like a handle

#if a 'Counts' table exists delete it, if not do nothing.
#execute is a method called on a cursor that says talk to the DB in SQL
cur.execute('DROP TABLE IF EXISTS Counts') #Without the IF statement it will 'traceback' if table doesn't exist

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''') #creates the DB Schema for a table in the db

#sets up a method to take a file as input
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
#identify  and select to parse from the file
for line in fh:
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1] #returns the email address
    #locate data that matches the select statement
    cur.execute('''SELECT count FROM counts WHERE email = ? ''', (email,)) #'?' is a placeholder, (email,)) is the parameter for input (avoids SQL injection)
    row = cur.fetchone() #return that data with a fetch method, #row is a list
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,)) #if email wasn't found, then insert it into the table with count of 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https:www.sqllite.org/lang_select.html
#the loop has finished and now we will rea9d the results of our updates to the Counts table.
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10' #top 10 counts descending

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1]) # for each row return column in ipos 0 and 1

cur.close() #close the cursor instance

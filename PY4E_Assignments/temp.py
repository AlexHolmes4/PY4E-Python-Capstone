
#read through a file, update to DB every organization that sent an email, and count the number of emails sent from each organization
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

orgdict = dict()
for line in fh:
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1] #returns the email address
    orgpos = email.find('@')
    org = email[orgpos+1:]
    orgdict[org] = orgdict.get(org, 0) + 1

print(orgdict)

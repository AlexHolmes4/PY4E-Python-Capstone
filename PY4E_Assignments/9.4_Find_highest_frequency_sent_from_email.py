name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

#make a histogram for email and count
counts = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

#find the highest frequency email occurance use .items() to allow two iteratives
bigemail = None
bigcount = None
for key,value in counts.items():
    if bigemail is None or value > bigcount:
        bigemail = key
        bigcount = value

print(bigemail,bigcount)
